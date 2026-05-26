print("Hello, World! 😎")
print("*" * 10)
2 + 3
x = 2

boleano = False
print(boleano)
if boleano:
    print("Es verdadero")
else:
    print("Es falso (No es verdadero)")

course = "Python for\n \"Beginners\""
long_message = """ --
Long string
with multiple lines
--ß"""

print(long_message)
print(len(course))

print(course[0:4])
print(course[0:])  # Imprime toda la cadena
print(course[:5])  # Imprime los primeros 5 caracteres
print(course[:])   # Imprime toda la cadena
fruit = "Apple"
# Imprime la cadena sin el primer y último carácter
print("-> " + fruit[1:-1])


# ********** 46:30
first = "Dianita"
last = "Fabila"
full = f"{first} {last}"
print(full)
print(len(full))
full2 = "{} {} {}".format(first, last, "!!!")
print(full2)
print(len(full2))
full3 = f"{len(first)} {2+2}"
print(full3)


course = " Python for Beginners "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())


print(course.find("for"))
# Verifica si "for" está presente en la cadena (!=> not in)
print("for" in course)
print(course.replace("Beginners", "Absolute Beginners"))
print(course)


print("------")
# Boolean comparations
print("bag" > "Apple")  # True, porque "b" es mayor que "A" en la tabla ASCII
# False, porque las letras mayúsculas y minúsculas son diferentes
print("bag" == "BAG")

print(ord("b"))
print(ord("B"))
