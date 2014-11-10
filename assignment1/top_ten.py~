import sys
import json

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

    for w in sorted(top_list, key=top_list.get, reverse = True)[:10]:
        print w, top_list[w]

if __name__ == '__main__':
    main()
