def with_custom_message(message):
    def with_message(function):
        print("{}:".format(message))
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return with_message

@with_custom_message("Hello")
def multiply(a, b):
    c = a * b
    print("the result of {} * {} is {}".format(a, b, c))

multiply(10, 2)