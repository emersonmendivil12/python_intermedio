#*Ejercicio CONT_VOCAL:* Contador de Vocales en un Texto (Bucle for y range)Pide al usuario que ingrese una frase o palabra. Utilizando un bucle for, recorre la cadena e imprime únicamente los números pares correspondiente a las posiciones/índices de los caracteres, junto con el carácter en dicha posición.

#Pista: Puedes combinar la función range() junto con len(texto) para iterar sobre los índices de la cadena.

texto:str = input("nunca pierdas la cabeza por un rabo: ")
i:int = 0

for letra in texto:
    if i % 2 == 0:
        print("Indice", i, ":", letra)
    i = i + 1

    