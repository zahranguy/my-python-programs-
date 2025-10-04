print("Calculator")

variable = input("Enter a value (no decimals): ")
variable2 = input("Enter another value (no decimals): ")

print("what do you want to do?")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("Enter choice(1/2/3/4): ")


if choice == "1":
    print(int(variable) + int(variable2))
if choice == "2":
    print(int(variable) - int(variable2))
if choice == "3":
    print(int(variable) * int(variable2))
if choice == "4":
    print(int(variable) / int(variable2))
if choice not in ["1", "2", "3", "4"]:
    print("invalid input")