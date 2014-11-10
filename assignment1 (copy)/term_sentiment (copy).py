import sys

import json

scores = {} # initialize an empty dictionary


def load_scores(afinnfile):
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def line_score(line):
    Total = 0
    words = line.split(" ")
    for word in words:       
       lword = word.encode('ascii', 'ignore').lower()
       if lword in scores.keys():
           Total = Total + scores[lword]
           ## print scores[lword]
    return Total
   
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    load_scores(sent_file)

    for line in tweet_file:
       score = 0
       tweet = json.loads(line)
       if "text" in tweet.keys():
          score = line_score(tweet['text'])
       print score

if __name__ == '__main__':
    main()
