# EXERCISE 18 Names, Variables, Code, Functions

def print_two(*args):
    arg1, arg2 =args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
        print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("i got nothing")

def print_more(**arg):
    print(arg)
print_more(name="Aldrin",age="23")

print_two("zed","Zed")
print_two_again("zed", "Zed")
print_one("first!")
print_none()