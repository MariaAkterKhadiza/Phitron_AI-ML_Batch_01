
# # for row in range(5):
# #     for col in range(row + 1):
# #         print("#", end = " ")
# #     print()


# ascii vale
#small lettter_97(a)
# for i in range(5):
#     for j in range(i+1):
#         print(chr(97+i), end = " ")
#     print()

#capital letter(65_A)
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+i), end = " ")
#     print()


# traversing nested list

bajar_list =[["alu",'piyaj'],[12,13,16,78],['pizza',2.5,30]]
for item in bajar_list:
    for choto_item in item:
        print(choto_item)