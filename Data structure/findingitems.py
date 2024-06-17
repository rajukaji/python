#finding items
letters = ["a", "b", "c"]

print(letters.index("b"))#finding the index of the object

#if not in the list, we get an effor, so using for in
if "d" in letters:
    print(letters.index("d"))


print(letters.count("d"))#number of occurances

