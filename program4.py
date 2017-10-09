# Function (program) to take in a list and return a new list with
# the elements of the former without duplicates

def remove_duplicate(alist):
  return list(set(alist))


alist = [1,1,1,2,3,3,4,8,8,9]
alist = remove_duplicate(alist)

print alist
