for number in range(5):
    print("Attempt", number+1, (number+1)*".")


for number in range(1, 10, 2):  # 3rd argument will be a step
    print("Attempt", number, number*".")


successful = True
for numero in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:  # if not breaked, will execute
    print("attempted 3 times and failed")


for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


print(type(5))
print(type(range(5)))  # => Iterable
# iterable
for x in "Phyton":
    print(x)

for n in [1, 2, 3, 4]:
    print(n)
#######################

numero = 100
while numero > 0:
    print(numero)
    numero //= 2


command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

count = 0
for exerciseNum in range(1, 10):
    if exerciseNum % 2 == 0:
        print(exerciseNum)
        count += 1

print(f"We have {count} even numbers")
