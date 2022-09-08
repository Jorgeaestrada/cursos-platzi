# Example 3
z = 5


def my_func_3():
    z = 3

    def my_other_func_2():
        z = 2
        print(z)

    my_other_func_2()

    print(z)


my_func_3()

print(y)
