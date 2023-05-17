# using a lambda to square a number
def my_func(n):
    return lambda x : x * n

doubler = my_func(5)
print(doubler(5))