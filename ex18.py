#names variables code fucntions

#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#that *arg is actually pointless instead do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this takes only one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this takes no arg
def print_none():
    print("I got none")

print_two("adi", "ram")
print_two_again("adi", "ram")
print_one("Jack")
print_none()