# set are mutable
set_val={1,2,3,4,5,4,5,6}
print(set_val)
print(f"type: {type(set_val)}")

empty={} # by default it will be dict then we have to use the set method to convert this into set
print(f"type: {type(empty)}")

empty_set=set({3,6,9,5})
print(f"type: {type(empty_set)}")


#its method
empty_set.add(2) # add to start
print(empty_set)

empty_set.remove(3)
print(empty_set)
# print(empty_set.clear())

# empty_set.pop()

empty_set.intersection(set_val)
print(empty_set)
