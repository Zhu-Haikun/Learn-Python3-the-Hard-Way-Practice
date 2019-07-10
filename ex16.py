# 从sys库中导入argv方法
from sys import argv
# 将filename的值赋于argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the tile...")
# 将filename变量以w模式打开，并将得到的内容赋于target变量
target = open(filename, 'w')

# print("Truncating the file. Goodbye!")
# # 对target变量使用truncate方法
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# 通过write方法将line1变量内容赋于target变量
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
# 对target变量使用close方法
target.close()
