''' variable scope examples'''
# Example 1
x = 5


def my_func_1():
    print(x)


def my_other_func_1():
    print(x)


my_func_1()
my_other_func_1()