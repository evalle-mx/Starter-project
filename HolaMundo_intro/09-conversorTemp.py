temperatura = float(input("Digite una temperatura: "))
escala = input("Digite la escala de la temperatura (C, F o K): ").upper()

# i.e.  20 c => 68.0 ; 100 F ==> 37.77..   ; 321 L => 'escala incorrecta'

if escala == 'C':
    print("Celsius")
    print(f"La temperatura en Celsius es: {temperatura * 9/5 + 32}") # (t-32) * 5/9
elif escala == "F":
    print("Farenheit")
    print(f"La temperatura en Farenheit es: {(temperatura - 32) * 5/9}") # t*1.8 +32
elif escala == "K":
    print("Kelvin")
    print(f"La temperatura en Kelvin es: {temperatura - 273.15}")
else:
    print("Escala incorrecta")
