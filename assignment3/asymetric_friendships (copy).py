import MapReduce
import sys

"""
Count friends given pairs friendA,FriendB as records
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

must_hold_global_list = []  # list previously handled people
map_of_people = {}

def mapper(record):    
    key = record[0]      # friendA
    word = record[1]     # friendB
    map_of_people[key]=1
    mr.emit_intermediate(record[0], record[1])

def reducer(person, list_of_friends):

    asymetric_list_for_person =[]
    for v in list_of_friends:
        if (v,person) not in must_hold_global_list:   #first appearance of v
            must_hold_global_list.append((person,v))
        else:
             must_hold_global_list.remove((v,person))

    del map_of_people[person]
    if len(map_of_people)==0: #if we emptied it
        for v in must_hold_global_list:
            mr.emit((v[0],v[1]))
            mr.emit((v[1],v[0]))
        


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
