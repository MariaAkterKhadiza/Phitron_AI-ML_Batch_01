# year = int(input())
# method_01

# if year % 400 == 0:
#     print("leap Year")
# elif year % 100 == 0:
#     print("Not leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not leap Year")


# metho_02

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not leap year")

    # method_03
    year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not leap year")

