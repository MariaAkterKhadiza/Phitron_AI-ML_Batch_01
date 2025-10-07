# input =  i love python
# turn into list = ['i', 'love', 'python']
# output = i evol nohtyp

a = input("")
a = a.split(" ")
print(a)
result = ""
for i in a:
    result += i[::-1] + " "
print(result)