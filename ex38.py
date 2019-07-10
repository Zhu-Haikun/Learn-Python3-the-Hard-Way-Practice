ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# 使用split函数以“空格”作为分割点，将字符串转化为列表
stuff = ten_things.split(' ')
print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

# 当stuff列表中元素数量等于10时停止循环
while len(stuff) != 10:
    # pop()函数会从目标列表中移动最后一个元素并返回这个元素
    # 除了用点语法来调用函数外，还可以使用最基本的函数调用方式
    # 比如 next_one = pop(more_stuff)，显然在编程的过程中应该尽量使用点语法和普通函数调用方式的组合
    # 多个点或者多个括号都不能让其代码阅读者明白其中的含义
    # 这两种函数调用方式的不同之处在于，使用点语法，python先会检测变量的类型，之后再去判断所调用函数是否可用于此类型
    # 而使用基本的函数调用方式并不存在这个问题，这可能存在类型强制转换的操作
    next_one = more_stuff.pop()
    # 当打印的函数只需要出现在字符串的最后时，不需要加入大括号，其他格式与正常打印变量的方式相同
    print("Adding: ", next_one)
    print("The 'more_stuff' list: ", more_stuff)
    # 将新的列表变量增加至stuff列表
    stuff.append(next_one)
    print("There are {} item now.".format(len(stuff)))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())  # 打印通过pop()函数移动的元素
print(stuff)    # 直接打印stuff列表，其以列表格式呈现
print(' '.join(stuff)) # 使用join()函数后，列表格式被间隔符取代
print('#'.join(stuff[3:5]))
# stuff[3:5]这是一种切片方式，可以定位列表中元素的位置
# 其中3的含义为索引为3的元素，5为序数，含义为第五个元素
