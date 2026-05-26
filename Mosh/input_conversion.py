
# int(x)  # Convierte la cadena a un número entero
# float(x)  # Convierte la cadena a un número decimal (float)
# bool(x)  # Convierte la cadena a un valor booleano (True si la cadena no está vacía, False si está vacía)
# str(x)  # Convierte el valor a una cadena (string)


# x = input("x: ")
# # print(type(x))
# y = int(x) + 1
# print(f"x: {x}, y: {y}")


# Booleans\

b1 = bool(0)
b2 = bool(1)
b3 = bool(-1)  # True, cualquier número diferente de 0 se considera True

print(f"b1: {b1}, b2: {b2}, b3: {b3}")
b1 = bool("")
b2 = bool("False")
b3 = bool(" ")  # True, cualquier cadena no vacía se considera True
print(f"b1: {b1}, b2: {b2}, b3: {b3}")
