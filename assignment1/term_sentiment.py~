import sys, string

import json

scores = {} # initialize an empty dictionary

##--------------------------------------------------------
## load_scores() loads the scores into a global dictionary
def load_scores(afinnfile):
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)        # Convert the score to an integer.

##--------------------------------------------------------
## message_average_score() computes the average score 
##                         for the words in the message
def message_average_score(line):
    Total = 0
    words = line.split(" ")
    no_words = 0
    for word in words:       
       lword = word.encode('ascii', 'ignore').lower()
       if len(lword) > 0:
           no_words = no_words+1
           if lword in scores.keys():
               Total = Total + scores[lword]
    if no_words>0:
       return float(Total)/no_words
    return 0

##--------------------------------------------------------
## clean_up_text() converts the string to ascii and lower case 
##                 and removes punctuation (and replaces it
##                 with the space. 
def clean_up_text(source):
    
    lowerc = source.encode('ascii', 'ignore').lower()   ## convert to lower case and ascii

    punct = set(string.punctuation)                     ## replace punctuation with white space
    dest = ''
    for ch in lowerc:
        if ch in punct:
            ch = ' '
        dest=dest+ch
    
    return dest

##--------------------------------------------------------
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    load_scores(sent_file)

    new_terms={}   ## initialise new dictionary

    for line in tweet_file:
        score = 0       
        tweet = json.loads(line)
        if "text" in tweet.keys():
            cleaned_message = clean_up_text(tweet['text'])
            score = message_average_score(cleaned_message)

            ## now add new words
            words = cleaned_message.split()
            for newword in words:
                if not newword in scores.keys():
                    if not newword in new_terms.keys():
                        ## new term, 1 occurence, 1 score
                        new_terms[newword] = (1,score)
                    else:
                        ## one more occurence, increase occurences, calculate new average
                        occ,new_score = new_terms[newword] 
                        ## Calculate the previous sum of scores from the average, 
                        ## add new score then divide by the new number of occurences 
                        ## to get new average
                        new_score = (new_score*occ + score)/occ+1
                    
                        new_terms[newword] = (occ+1,new_score)
     
    ## Finished, output the new dictionary 
    for term in new_terms:
        occ,score = new_terms[term]
        print '%s %.3f' %(term, score)

if __name__ == '__main__':
    main()
