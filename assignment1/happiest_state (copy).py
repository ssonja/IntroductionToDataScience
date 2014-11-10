import sys
import string
import json

scores = {} # initialize an empty dictionary

def load_scores(afinnfile):
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)        # Convert the score to an integer.

def line_score(line):
    Total = 0
    words = line.split(" ")
    for word in words:       
        lword = word.encode('ascii', 'ignore').lower()
        if lword in scores.keys():
            Total = Total + scores[lword]
    return Total

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    happiness_loc = {}

    load_scores(sent_file)

    for line in tweet_file:
        score = 0
        tweet = json.loads(line)
        if "text" in tweet.keys():
            score = line_score(tweet['text'])
            if "place" in tweet.keys() and tweet["place"] is not None:
                place = tweet["place"]     ## get the place object              
                country_code = place["country_code"]
                if  country_code == "US" and place["full_name"] is not None:
                    citty,state = place["full_name"].split(', ')
                    if state in states.keys():
                        ## it is a valid state name       
                        if not state in happiness_loc.keys():                    
                            happiness_loc[state] = (1,score)        ## new state, 1st occurence, 1 score
                        else:
                            ## one more occurence, increase occurences, calculate new average
                            occ,new_score = happiness_loc[state] 
                            ## Calculate the previous sum of scores from the average, 
                            ## add new score then divide by the new number of occurences 
                            ## to get new average
                            new_score = (new_score*occ + score)/occ+1
                    
                            happiness_loc[state] = (occ+1,new_score)       
    max_score = 0
    for state  in happiness_loc.keys():
        occ,score = happiness_loc[state]
        if score > max_score:
            max_score = score
            happiest_state = state

    print happiest_state

if __name__ == '__main__':
    main()
