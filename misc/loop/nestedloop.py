#nested loop
#rows and columns

rows = int(input("How many rows? ::"))
columns = int(input("How many columns? ::"))
symbol = input("Enter a symbol :: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")#dont end in a new line
    print()#end in a new line

    