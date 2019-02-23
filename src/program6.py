total = 0
values = 0

with open('sum.txt', 'r') as inp:
   for line in inp:
           num = float(line)
           total += num
           values += 1

print('#  : ' + str(values))
print('Tot: ' + str(total))
print('Avg: ' + str(total/values))
