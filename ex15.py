# 调用argv函数
from sys import argv
# 将argv参数赋给filename变量
script, filename = argv
# 对filename变量执行open命令，并将结果赋给变量txt
txt = open(filename)

print(f"Here's your file {filename}:")
# 对txt变量执行read命令后打印结果
print(txt.read())

print("Type the filename again:")
# 输入文件名称，并将名称赋给file_again变量
file_again = input("> ")
# 对file_again变量执行open命令，并将结果赋给txt_again变量
txt_again = open(file_again)
# 对txt_again变量使用read方法，并将结果打印
print(txt_again.read())

print(txt.close())
print(f"The {filename} has been closed.")

print(txt_again.close())
print(f"The {file_again} has been closed too.")
