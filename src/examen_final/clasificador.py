#*Ejercicio CLASIFICAADOR*: Clasificador de Clima (Condicionales if-elif-else)Escribe un programa que pida al usuario la temperatura actual en grados Celsius (número decimal) y muestre un mensaje según los siguientes rangos:
#- Si es menor a 10: "Mucho frío"
#- Si está entre 10 y 25 (inclusive): "Clima templado"
#- Si está entre 26 y 35 (inclusive): "Clima cálido"
#- Si es mayor a 35: "Alerta de calor extremo"
temp= float(input("Ingresa la temperatura en Celsius: "))

if temp < 10:
    print("Mucho frio")
elif temp <= 25:
    print("Clima templado")
elif temp <= 35:
    print("Clima calido")
else:
    print("Alerta de calor extremo")






















