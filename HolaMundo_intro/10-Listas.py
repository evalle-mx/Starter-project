lenguajes = ["Python", "Java", "C++", "JavaScript", "React", "PHP"]  # Crea una lista de lenguajes de programación
print(lenguajes)  # Imprime la lista completa
print(lenguajes[1])  # Imprime el primer elemento de la lista
lenguajes[1] = "GO"
print(lenguajes)  # Imprime la lista actualizada
print  (lenguajes[1:4])  # Imprime los elementos desde el índice 1 hasta el índice 3
print(lenguajes[:3])  # Imprime los primeros 3 elementos de la lista
print(lenguajes[3:])  # Imprime los elementos desde el índice 3 hasta el ultimo elemento de la lista
print(lenguajes[-2])  # Imprime el penúltimo elemento de la lista (-1 ultimo elemento, -2 penúltimo elemento, etc.)

### 11-ListaMetodos.py
lenguajes.append("Ruby")  # Agrega un nuevo elemento al final de la lista
print(lenguajes)  # Imprime la lista con el nuevo elemento
lenguajes.insert(2, "C#")  # Inserta un nuevo elemento en la posición 2
print(lenguajes)  # Imprime la lista con el nuevo elemento
lenguajes.remove("C++")  # Elimina el elemento "C++" de la lista
print(lenguajes)  # Imprime la lista después de eliminar el elemento
del lenguajes[0]  # Elimina el primer elemento de la lista
print(lenguajes)  # Imprime la lista después de eliminar el primer elemento
print(len(lenguajes))  # Imprime la cantidad de elementos en la lista

print( "PHP" in lenguajes)  # Verifica si "PHP" está en la lista y devuelve True o False

lenguajes.clear()  # Elimina todos los elementos de la lista
print(lenguajes)  # Imprime la lista vacía