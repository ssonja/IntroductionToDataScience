import MapReduce
import sys

"""
Count friends given pairs friendA,FriendB as records
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):    
    key = record[0]          # friendA
    word = record[1]     # friendB

    mr.emit_intermediate(record[0], record[1])

def reducer(person, list_of_friends):

    total=0
    for v in list_of_friends:
        total +=1
    mr.emit((person,total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
