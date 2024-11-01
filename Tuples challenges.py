# Check for Number
friends = (3, 5, 7, 8, 10, 2, 50, 4)
guess = int(input("Pick a number"))

if guess in friends:
    print("Yes")
else:
    print("No")

# Third from last

num = ("one","two","three","four","five","six","seven","eight")
print(num[-3])
print(num[5])
print(num[0:4])