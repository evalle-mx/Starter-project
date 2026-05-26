# 1 - Perform a Task
def greet(first_name, last_name):
    print("Hi there")
    print(f"Welcome {first_name}")


greet("Netto", "speed")


# 2 - Return a value
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
file = open("greeting.txt", "w")  # write to a file
file.write(message)
file.close()


def increment(number, by):
    return number+by


print(increment(2, by=1))


# Optional Params
def increment2(number, by=2):
    return number+by


print(increment2(2, 5))


def multiply(x, y):
    return x*y


def multiply(*numbers):
    # print(numbers)
    total = 1
    for num in numbers:
        total *= num
    return total


mult = multiply(2, 3, 4, 5)
print(mult)
