# Read a Specific Number of Characters
number = int(input("How many characters do you want to print?"))
file = open("example.txt", "r")
print(file.read(number))
print(file.readline(number))
file.close()

# How Many Lines?

file = open("example.txt", "r")
data = file.read()
words = data.split()
print(len(file.readlines()))
file.close()