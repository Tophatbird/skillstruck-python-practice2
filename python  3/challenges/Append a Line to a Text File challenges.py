# Pen Pal
file = open("letter.txt", "a")
file.write("From your Pen Pal")
file.close()

file = open("example.txt")
print(file.read())


# Give Credit
file = open("report.txt", "a")
file.write("Quote was said by Gandhi")
file.close()

file = open("report.txt")
print(file.read())