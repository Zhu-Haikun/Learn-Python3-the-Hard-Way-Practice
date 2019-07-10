# 定义函数cheese_and_crackers，使其能够传入两个变量cheese_count与boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# 打印 We can just give the function numbers directly:
print("We can just give the function numbers directly:")
# 调用函数cheese_and_crackers，并传入20与30作为参数
cheese_and_crackers(20, 30)

# 打印 OR, we can use variables from our script:
print("OR, we can use variables from our script:")
# 为变量amount_of_cheese赋值为10
amount_of_cheese = 10
# 为变量amount_of_crackers赋值为50
amount_of_crackers = 50
# 调用函数cheese_and_crackers，并传入两个变量
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 打印 We can even do math inside too:
print("We can even do math inside too:")
# 调用函数cheese_and_crackers并传入参数10+20与5+6
cheese_and_crackers(10 + 20, 5 + 6)

# 打印 And we can comine the two, variables and math:
print("And we can comine the two, variables and math:")
# 调用函数cheese_ande_crackers，同时在传入变量时各加上100
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
