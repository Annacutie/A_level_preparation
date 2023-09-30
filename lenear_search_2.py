MyList = [1, 4, 3, 12, 0, 1, 9]
searchValue = int(input("Enter a value to be found: "))
found = False

for index in range(len(MyList)):
    if MyList[index] == searchValue:
        found = True
        break

if found:
    print(f"Value found at location {index}.")

else:
    print("Value not found.")