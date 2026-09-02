## crear un programa de login que mientras quela persona no ponga el usuario/contraseña correcto le siga pidiendo esa informacion, siel usuario/contraseña son correctos entonces darle un mensaje de bienvenida y salir delprograma
intentos:int=0
usuario_correcto:str="admin"
contraseña_correcta:str="1234"
while True:
    usuario:str=input(" ingrese Usuario: ")
    contraseña:str=input("ingrese la Contraseña: ")
    if usuario==usuario_correcto and contraseña==contraseña_correcta:
        print("Bienvenido!")
        break
    else:
        print("Error sigue intentando")
