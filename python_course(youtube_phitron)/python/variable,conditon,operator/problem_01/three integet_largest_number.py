

#method_01
a = int(input())
b = int(input())
c = int(input())

# if a >= b:
#     if a>= c:
#         print(a, "is the largest")
#     else:
#         print(c,"is the largest")
# else:
#     if b>= c:
#         print(b,"is the largest")
#     else:
#         print(c,"is the largest")

#method_02

if a>=b and a>=c:
    print(a,"is the largest")
elif b>=a and b>=c:
    print(b,"is the largest")
else:
    print(c,"is the largest")