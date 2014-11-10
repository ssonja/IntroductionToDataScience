import MapReduce
import sys

"""
Multiply matrixes
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

#record is an element of a matrix: (name,row_no,col_no,value)
def mapper(record):    
   for k in range (0,5):
       if record[0]=='a':
           mr.emit_intermediate((record[1],k), (record[2],record[3])) # k is the column value
       else:
           mr.emit_intermediate((k, record[2]), (record[1],record[3]))  # k is the row value

def reducer(pair, list_of_values):

    total =0
    for k in range (0,5):      
        add1 = 0
        add2 = 0
        for v in list_of_values:
            if v[0]==k:
                if add1 ==0:
                    add1=v[1]
                else:
                    add2=v[1]
        total+=add1*add2
                     
    
    mr.emit((pair[0],pair[1], total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
