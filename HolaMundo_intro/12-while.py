lenguajes = ["Python", "Java", "C++", "JavaScript", "React", "PHP"]  # Crea una lista de lenguajes de programación

i = 0  # Inicializa un contador
while i < len(lenguajes):
    print(lenguajes[i])
    i += 1


# El código anterior utiliza un bucle while para iterar a través de la lista de lenguajes de programación y imprimir cada uno de ellos. El contador 'i' se incrementa en cada iteración hasta que alcanza el tamaño de la lista.
print(". Fin del bucle while\n")
# 13-for.py
for lenguaje in lenguajes:
    print(lenguaje)