#Reading files
from sys import argv #import argv
script, filename = argv #argument
txt = open(filename)
print(f"Here's your file{filename}")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())