# Addition of numbers using derocators 


def sumx(func):
    def wrapper(*args, **kwargs):
        result = sum(args)
        return func(result, **kwargs)

    return wrapper


@sumx
def sum_numbers(result):
    return "sum of numbers is {0}".format(result)


print(sum_numbers(1, 2, 3, 4))

# sum of numbers is 10


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Before the function call
# Hello!
# After the function call