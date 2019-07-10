from sys import argv
# read the WYSS section for how to run this
# 将argv解包，其特性赋给script, first, second, third这四个参数
script, first, second, third = argv
test = input("How old are you?")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print(f"So, you are {test} old.")
