# N = int(input())

# count_yes = 0
# count_no = 0

# for i in range(N):
#     vote = input().strip()
#     if vote == "YES":
#         count_yes +=1
#     else:
#         count_no +=1


# if count_yes >= count_no:
#     print("ACCEPT")
# else:
#     print("REJECT")


n=int(input())
yes=0
no=0

for i in range(n):
    vote=input()
    if vote=="yes":
      yes=yes+1

else:
    no=no+1

if yes>no:
    print("ACCEPT")
else:
    print("REJECT")