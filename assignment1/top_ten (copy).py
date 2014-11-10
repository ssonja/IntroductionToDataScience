import sys
import json
import itertools

class HashItem(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

def getKey(hasht):
    return hasht.number

def main():
    tweet_file = open(sys.argv[1])

    top_list = {}

    for line in tweet_file:
       tweet = json.loads(line)
       if "entities" in tweet.keys():
          entities = tweet["entities"]
          if "hashtags" in entities.keys():
              hashtags = entities["hashtags"]
              for tagobj in hashtags:
                  tag = tagobj["text"]                  
                  if not tag in top_list.keys():                    
                      top_list[tag] = 1 
                  else:

                      top_list[tag] += 1
    print top_list

    new_order = {}

    new_order = sorted(top_list, key=top_list.get, reverse=False)

    print new_order

    top_ten = new_order[:10]
    
    for w in top_ten:
        print w

if __name__ == '__main__':
    main()
