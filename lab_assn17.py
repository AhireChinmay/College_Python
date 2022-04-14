file = open("new.txt","r")
lines = 0
words = 0
characters = 0
frequency = 0
for line in file:
    line = line.strip("\n")

words = line.split()
lines += 1
words += len(words)
characters += len(line)
frequency += len(line)

file.close()

print(f'''No of lines are: {lines}
No of words are: {words}
No of characters are: {characters}
The frequency is {frequency}''')

