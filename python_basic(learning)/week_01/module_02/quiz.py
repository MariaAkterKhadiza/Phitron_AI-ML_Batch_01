#q_1
x = 5
if x > 3:
    print("A")
elif x > 1:
    print("B")
else:
    print("C")

#q_2
i = 0
while i< 3:
    i += 1
    if i == 2:
        break
    print("Done")
#q_03
for i in range(2):
    for j in range(3):
        if j == 1:
            break
        print(i, j)

#q_4
for i in range(3):
    if i == i:
        break
    print(i)
 
 #q_5
for i in range(5):
    if i == 2:
        break
    print(i, end="")
#q_6
count = 0
for n in [1,2,3,4,5]:
    if n % 2 !=0:
        continue
    count +=1
    print(count)
# #q-7
s = 0
for i in range(1, 5):
    if i % 2 == 0:
        s +=i
    else:
        s -=i
print(s)
# #q-8
for i in range(5, 0, -1):
    if i % 2 == 0:
        continue
    if i == 3:
        break
    print(i, end=" ")