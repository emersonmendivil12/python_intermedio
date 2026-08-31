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
