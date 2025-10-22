print("Calculator")

variable = input("Enter a value: ")
try:
    float(variable)
except ValueError:
    print("how is that a number?")
    exit()

print("what do you want to do?")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("Enter choice(1/2/3/4): ")


variable2 = input("Enter another value: ")
try:
    float(variable2)
except ValueError:
    print("how is that a number?")
    exit()


if choice == "1":
    print(float(variable) + float(variable2))
if choice == "2":
    print(float(variable) - float(variable2))
if choice == "3":
    print(float(variable) * float(variable2))
if choice == "4":
    print(float(variable) / float(variable2))
if choice not in ["1", "2", "3", "4"]:
    print("invalid input")
