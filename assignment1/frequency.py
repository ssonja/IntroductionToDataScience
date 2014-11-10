import sys, string

import json

def clean_up_text(source):

    ## convert to lower case and ascii
    lowerc = source.encode('ascii', 'ignore').lower()

    ## replace punctuation with white space
    punct = set(string.punctuation)
    dest = ''
    for ch in lowerc:
        if ch in punct:
            ch = ' '
        dest=dest+ch
    
    return dest

def main():
    tweet_file = open(sys.argv[1])

    terms={}   ## initialise dictionary
    
    total_number_of_words =0

    for line in tweet_file:
       tweet = json.loads(line)
       if "text" in tweet.keys():
          cleaned_message = clean_up_text(tweet['text'])
          ## get new words
          words = cleaned_message.split()
          for word in words:
                total_number_of_words += 1
                if not word in terms.keys():
                    ## new term, 1st occurence
                    terms[word] = 1
                else:
                    ## one more occurence, increase occurences
                    terms[word] += 1

    ## Finished, output the dictionary 
    for term in terms.keys():
       freq = float(terms[term])
       freq /= total_number_of_words
       print term, freq

if __name__ == '__main__':
    main()
