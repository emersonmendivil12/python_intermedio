#1 escriba un programa que asepte la opcion de dos jugadores en piedra-papel 
#- entrada : persona1= piedra,persona2=papel
#salida:gana  persona2, papel enbuelve a piedra
persona1 = "piedra"
persona2 = "papel"

if persona1 == "piedra" and persona2 == "papel":
    print("gana persona2, papel enbuelve a piedra")
else:
    print("gana persona1, papel enbuelve a piedra")
#2 escribe un programa que asepte 3 numeros y calcule el minimo 
#-entrada :7,4,8
#salida: 4  
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 <= num2 and num1 <= num3:
    minimo = num1
elif num2 <= num1 and num2 <= num3:
    minimo = num2
else:
    minimo = num3

print(minimo)