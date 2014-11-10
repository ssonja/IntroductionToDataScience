import MapReduce
import sys

"""
Trim DNA sequence
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

#record is a pair: id, string
def mapper(record):    
    trimmed = record[1][:-10]
    mr.emit_intermediate(trimmed,1)

def reducer(trimmed, list_of_values):
   mr.emit(trimmed)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
