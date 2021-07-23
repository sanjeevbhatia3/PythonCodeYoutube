def function1(function):
    def wrapper():
        print("hello")
        function()
        print("Welcome to python tutorial")
    return wrapper

def function2():
    print("pythonista")

my_func = function1(function2)
my_func()