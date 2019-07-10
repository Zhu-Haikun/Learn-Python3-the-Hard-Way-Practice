from sys import argv

script, input_file = argv

def print_all(f):
#使用“<<<”之后的部分，这是一种debug方式，因为有时候总有人会问，值是怎么变化的，但是光通过看是看不明白的
    print(">>> print_all: f=", f)
    print(f.read())
    print("<<< print_all: f=", f)

def rewind(f):
# 将文件读写位置移动到开头，具体见习题16
    f.seek(0)

def print_a_line(line_count, f):
    print(f">>> print_a_line: line_count = {line_count}")
    print(line_count, f.readline(), end="")
    print(f"<<< print_a_line: line_count = {line_count}")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
