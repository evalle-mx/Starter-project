texto = "Hola Mundo"
print(texto)
print(texto.upper())
print(texto.lower())
# Devuelve la posición de la primera aparición de "Mun" (-1 si no se encuentra)
print(texto.find("Mun"))
print(texto.replace("Mundo", "Python"))
nuevoTexto = texto.replace("Mundo", "Python")
print(texto, nuevoTexto)
print("Mundo" in texto)  # Verifica si "Mundo" está presente en el texto

print(texto.startswith("Hola"))  # Verifica si el texto comienza con "Hola"
print(texto.endswith("Mundo"))  # Verifica si el texto termina con "Mundo"


print(texto.count("o"))  # Cuenta cuántas veces aparece la letra "o" en el texto
# Devuelve la posición de la primera aparición de "Mundo" (genera un error si no se encuentra)
print(texto.index("Mundo"))
# Verifica si el texto solo contiene letras (False en este caso por el espacio)
print(texto.isalpha())
# Verifica si el texto solo contiene dígitos (False en este caso)
print(texto.isdigit())
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

print(texto.split())
print(texto.split(" "))
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())
print(type(texto))
print(len(texto))
print(texto[0])


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
