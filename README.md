# CONTROL DE FLUJO
## Condicionales
### la sentencia if 
esta sentencia al igual a otros lenguajes de programacion  en su escritura devemos añadir exprecion de comparacion terminando en ":"
```python
temperatura: float =40.0
if temperatura  > 20 : 
print ("alta temperatura")
```
en este caso solo se ejecutara el bloque ''if'' si la condicion es verdadera, para controlar si la condcion es falsa devemos usar la sentencia else 
```python
temp:int =20
if temp >35:
    print("temperatura alta ")
    else 
    print("temperatura normal")
```
podriamos tener muchas condicionales lo que se llamaria condiciones anidas
```python
temp:int=20
if temp <10:
    pint("nivel azul mucho frio ")
    else:
        pint("nivel verde normal ")
        else:
        if temp <30:
            pint("nivel naranja")
        else:
            print("nivel rojo ")
```
python ofrece una mejora en 1 escritura de condiciones anidadas, para ello  podemos usar  
```python
temp:int=20
if temp <10:
    pint("nivel azul mucho frio ")
    else:
        pint("nivel verde normal ")
    elif temp <30:
        pint("nivel naranja")
    
     else:
        print("nivel rojo ")
```

### sentencia match-case 
esta es unja nueva centencia condicional similar a los if anidados 
```python
vocal:str="a"
match vocal:
    case "a":
        print("es una vocal")
    case "e":
        print("es una vocal")
    case "i":
        print("es una vocal")
    case "o":
        print("es una vocal")
    case "u":
        print("es una vocal")
    case _:
        print("es un consonante")
```
una manera de aser el codigo es :
```python
vocal:str=input("ingrese una letra: ")
match vocal:
    case "a" | "e" | "i" | "o" | "u":
        print("es una vocal")
    case _:
        print("es una consonante")

```
## bucles 
### la sentencia while es el primer mecanismo que existe en python para repetir instrucciones.
la semantica tras esta centensia es mientras se cumpla la condicion as algo 
ejemplo 
```python
 salir:str="N"
while salir=="N":
    print("Hol que taal")
    salir=input("deseas salir (S/N): ")
print("Adios")
```
se  puede de un "while" asiendo el uso de "break" 
```python
intentos:int=0
respuesta_correcta:str="ayacucho"
while intentos<3:
    respuesta_usuario:str=input("Capital Ayacucho: ")
    if respuesta_correcta==respuesta_usuario:
        print("respuesta correcta")
        break
    else:
        print("Error si intentando")
    
    
    intentos=intentos+1
print(intentos) 
```
### la sentencia for
python permite recorrer aquellos tipos de datos que sean **iterables**.
Algunos ejemplos de tipos de datos que permiten ser iterados son: cadenas de 
texto, listas, diccionarios, ficheros.
```python
nombre:str="gargamel" # string, texto, cadena de texto
amigos:list[str]=['pepe','lucho','juan'] # lista de texto
alumno:dict[str:int|str]={
    "dni":76543298,
    "nombre":"juncito"
} # diccionario
### la sentencia for

A continuacion planteamos un ejemplo en el que vaamos a 
recorrer una cadena de texto:
```python
texto:str="hola mundo"
for letra in texto:
    print(letra)
```
La clave para entender el ejercicio es darse cuenta que el bucle va tomando en 
cada iteración, cada uno de los elementos de la variable. 
En el ejemplo 'letra' va tomando cada una de las letras que tiene 'texto'.
La variable 'letra' puede tomar cualquier nombre.

**Romper un bucle for**
Al igual que `while`, para romper o terminar un bucle `for` debemos usar `break`.
*ojo* - para realizar la rotura se debe previamente cumplir una condicional
## crear un programa que recorra un texto y que termine la ejecucion cuando encuentra la letra a
```python
texto:str="holis de donde eres y a donde vas"
for l in texto:
    if l == "a":
        break
    else:
        print(l)
```
**secuencias de numeros**
Es my habitual hacer uso de secuencias en bucles, python aporta una funcion 
para reaalizar la secuencia de numeros `range()`, esta funcion devuelve o 
retornaun flujo de numeros en el rango especificado.
su estructura es la siguiente:     

- `start` - es *opcional* y tiene valor por defecto `0`
- `stop` - es *obligatorio* (este valor siempre llega a 1 menos que el valor asignado)
- `step` - es *opcional* y tiene valor por defecto `1` es el valor que ira incrementado.
```python
##1. desemos mostra ls numeros del 0 al 5 con la funcion range
for numero in range(6):
    print(numero)
print("-----------------")

##2. Deseamos mostrar los numers del 2 al 6
for numero in range(2,7):
    print(numero)
print("-----------------")

##3. mostrar los numeros pares que existen entre 1 y 10
for pares in range(2,11,2):
    print(pares)

```
> [!TIP] Se suele utilizar nombres de variables `i,j,k` paara 
lo que se denomina `contadores`. o la variable que va despues 
del `for`.



