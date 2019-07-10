# i = 0
# numbers = []
#
# while i < 6:
#     print("At the top i is {}".format(i))
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is {}".format(i))
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)
def count_number(i, x, n):
    list = []
    while i < x:
        print("At the top i is {}".format(i))
        list.append(i)

        i += n
        print("Numbers now: ", list)
        print("At the bottom i is {}".format(i))
    return list

numbers = count_number(0, 7, 2)

print("The numbers: ")
for num in numbers:
    print(num)
