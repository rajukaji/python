with open('file.txt', 'r') as file1:
    file = file1.read()
    print(file)
# using with open() because, it automatically closes file
# need not use file.close()

print(file)

