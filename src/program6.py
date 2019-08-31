
# variables to hold the values
total = 0
values = 0

myList = []

with open('sum.txt', 'r') as inp:
    # to take in malformatted Values (remove try/except block)

  
       for line in inp:
           try:
               num = float(line)
               total += num
               values += 1
               myList.append(num)
           except ValueError: 
           #this catches the error where the file may contain non-numerical characters
               i = 1
# sort the list
myList.sort()
#make a copy of the list
list2 = list.copy(myList)

print('# Values   : ' + str(values))
if (values == 0):
    print('All values are 0')
if (values == 1):
    print('All values are ' + str(total))
else:

    print('Sum Total : ' + str(total))
    print('Avgerage   : ' + str(total/values))
    print('Sorted asc : ' + str(myList))

    # reverse the myList
    list2.reverse()

    #print new reversed list
    print('Sorted desc: ' + str(list2))
