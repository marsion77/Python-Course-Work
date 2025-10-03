def my_decortaors(func):
    def wrapper():
        print("Top Decors")
        func()
        print("Bottom Decors")
    return wrapper


@my_decortaors
def greet():
    print("Hello World")

greet()
    
