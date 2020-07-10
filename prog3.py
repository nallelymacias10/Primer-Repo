
print("S.Suma \n R.Resta \n D.Division \n M.Multiplicacion \n A.Salir ")
opcion = ""
menu= True
while menu ==True:
    opcion = input("Que opcion elige: ")
   
    if opcion == 'S':
        num1 = ("Ingrese un numero \n")
        num2 =("Ingrese otro numero \n")
        resul = num1+num2
        print(f'La suma de los numero es: {resul}')
    if opcion == 'R':
        num1 =  ("Ingrese un numero \n")
        num2 =("Ingrese otro numero \n")
        resul = num1-num2
        print(f'La resta de los numeros es: {resul}')
    if opcion == 'D':
        num1 = ("Ingrese un numero \n")
        num2 = ("Ingrese otro numero \n")
        resul = num1/num2
        print(f'La division de los numeros es: {resul}')
    if opcion == 'M':
        num1 = ("Ingrese un numero \n")
        num2 = ("Ingrese otro numero \n")
        resul = num1*num2
        print(f'La multiplicacion de los numeros es: {resul}')
else:
   print("Fin del programa")
    
    