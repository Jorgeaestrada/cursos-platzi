def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, "solo puedes utilizar cadenas"
        return string * n

    return repeater


def make_division_by(n):
    """
        This closure returns a function that returns the division
        of a number by n
    """
    return lambda x: x/n


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Never Settle "))

    repeat_10 = make_repeater_of(10)
    print(repeat_10("Don't give up "))

    divide_3 = make_division_by(3)
    print(divide_3(15))

    divide_10 = make_division_by(10)
    print(divide_10(200))


if __name__ == "__main__":
    run()
