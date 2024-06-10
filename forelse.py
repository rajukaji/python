names = ["petay", "motey"]
found = False
for name in names:
    if name.startswith("r"):
        print("Found")
        found = True
        break
else:
    print("Not Found")