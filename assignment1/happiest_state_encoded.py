import sys
import string
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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
              country_code.encode('ascii', 'ignore')
              if  country_code == "US" and place["full_name"] is not None:
                citty,state = place["full_name"].split(', ')
                astate = state.encode('ascii', 'ignore')
                if not astate in happiness_loc.keys():
                    ## new state, 1st occurence, 1 score
                    happiness_loc[astate] = (1,score)
                else:
                    ## one more occurence, increase occurences, calculate new average
                    occ,new_score = happiness_loc[astate] 
                    ## Calculate the previous sum of scores from the average, 
                    ## add new score then divide by the new number of occurences 
                    ## to get new average
                    new_score = (new_score*occ + score)/occ+1
                    
                    happiness_loc[astate] = (occ+1,new_score)                  
                print state, score
    max_score = 0
    for state  in happiness_loc.keys():
       occ,score = happiness_loc[state]
       if score > max_score:
          max_score = score
          happiest_state = state

    print "The happiest state is: ",states[happiest_state], ", score: ", max_score

if __name__ == '__main__':
    main()
