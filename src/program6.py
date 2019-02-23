total = 0
values = 0

list = []
with open('sum.txt', 'r') as inp:
    # to take in malformatted Values (remove try/except block)

    # data = inp.read()
    # data.replace("[],abcdefghijklmnopqrstuvwxyz!@#$%^&*()_~`'{}<>?/;:", "")
    # for line in data:
        # line =  line.remove("[]", '')

       for line in inp:
           try:
               num = float(line)
               total += num
               values += 1
               list.append(num)
           except ValueError:
               i = 1

list.sort()
reversed = list.reverse()

print(reversed)
print('# Values   : ' + str(values))
if (values == 0):
    print('All values are 0')
if (values == 1):
    print('All values are ' + str(total))
# if(values > 1):
else:

    print('Comp Total : ' + str(total))
    print('Avgerage   : ' + str(total/values))
    print('Sorted asc : ' + str(list))

    # reverse the list
    list.reverse()
    print('Sorted desc: ' + str(list))
