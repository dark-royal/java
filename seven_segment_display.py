# for i in range(7):
#     for j in range(10):
#         print("*",end ='')
#     print()
#
# var = input("lol")
# for i in range(7):
# print("*********")
# print("*        *")
# print("*        *")
# print("*        *")
# print("**********")
# print("*        *")
# print("*        *")
# print("**********")

lio = [True, True, True, True, True, True, True]
inp = int(input("Enter segment"))

for i in range(7):

    if inp == 0:
        lio[i] = False


    if lio[0]:
        print("*        ")
    if lio[1]:
        print("*", end='')
    if lio[2]:
        print("        *")
    if lio[3]:
        print(" ********")
    if lio[4]:
        print("*        ")
    if lio[5]:
        print("*", end='')
    if lio[6]:
        print("*", end='')

    # if lio[7]:
    #     print("        *")
    #
