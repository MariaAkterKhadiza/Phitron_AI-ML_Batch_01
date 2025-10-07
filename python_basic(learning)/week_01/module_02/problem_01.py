inp = input()
numbers = inp.split()
#print(numbers)


x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[2])

min = x
max = x

#min
if min > y :
    min = y
if min > z :
    min = z



#max
if y > max:
    max = y

if z > max:
    max = z

print(min , max)
