MyList = [1, 4, 3, 12, 0, 1, 9]
searchValue = int(input("Enter a value to be found: "))
MaxIndex = len(MyList) - 1
found = False
Index = -1

while found == False and Index < MaxIndex:
    Index = Index + 1
    if MyList[Index] == searchValue:
        found = True

if found:
    print(f"Value found at location {Index}.")

else:
    print("Value not found.")