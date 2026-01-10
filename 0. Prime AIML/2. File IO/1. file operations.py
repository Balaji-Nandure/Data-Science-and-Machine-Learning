# File reading
# file = open('0. Prime AIML/2. File IO/sample.txt', 'w')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close() #dont forget to close the file

# File writing
file = open('0. Prime AIML/2. File IO/sample.txt', 'w')
file.write('This is overwritten data')
file.close()

# File appending
file = open('0. Prime AIML/2. File IO/sample.txt', 'a')
file.write('This is appended data')
file.close()
