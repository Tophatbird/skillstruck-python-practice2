# Never Mind
file = open("email.txt", "w")
file.write("Never mind")
file.close()

#Custom Greeting Cards
answer = input("What would you like on your card?")
file = open("report.txt", "w")
file.write(answer)
file.close()
print(file.read())