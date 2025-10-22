a = 99

while a > 1:
    print(a, "bottles of beer on the wall,")
    print(a, "bottles of beer,")
    print("Take one down, pass it around,")
    a = a - 1
    print(a, "bottles of beer on the wall.\n")
while a == 1:
    print(a, "bottle of beer on the wall,")
    print(a, "bottle of beer,")
    print("Take one down, pass it around,")
    print("No bottles of beer on the wall.\n")
    a = a - 1
    if a == 0:
        print(" No bottles of beer on the wall, \n No bottles of beer. \n Go to the store, buy some more, \n 99 bottles of beer on the wall.")
        exit