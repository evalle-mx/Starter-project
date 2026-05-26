temperature = 10
if temperature > 30:
    print("it's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
elif temperature > 10:
    print("It's cold")
else:
    print("It's very cold")


print("Done")


age = 12

if age >= 18:
    message = "You are an adult"
else:
    message = "You are a child"

message2 = "Elegible to vote" if age >= 18 else "Not elegible to vote"
print(message)
print(message2)


# . LOGICAL OPERATORS
high_income = True
good_credit = bool(1)
student = True

if high_income and good_credit:  # and|or
    if not student:
        print("Elegible for loan")
    else:
        print("Not Elegible for loan (is student)")
else:
    print("Not elegible")


if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
