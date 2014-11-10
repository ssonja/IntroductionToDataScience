import MapReduce
import sys

"""
Count friends given pairs friendA,FriendB as records
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):    
                        # friendA    friendB
    mr.emit_intermediate((record[1], record[0]),1)  
    mr.emit_intermediate((record[0], record[1]),1)


def reducer(pair, list_of_values):
    if len(list_of_values) == 1:
        mr.emit(pair)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
