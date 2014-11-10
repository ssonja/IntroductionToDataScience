import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):    
    tbl = record[0]          # table name
    order_id = record[1]     # order_id

    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_records):
    # key: order_id
    # list_of_records: list of records from both databases

    for v in list_of_records:
        if v[0]=='order':
            out=[]
            for w in list_of_records:
                if w[0]=='line_item':
                    out=v+w
                    mr.emit(out)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
