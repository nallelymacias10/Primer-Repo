#escribe un programa que pida al usuario un texto y un numero entero.
#MAndar a imprimir en pantalla el texto repetido las veces indicado 
#por el numero
#Hacer el programa usuando una funcion

def repetir (texto,numero):
    print(texto*numero)
    
t= input("Ingresa un texto: ")
n= int(input("Ingresa un numero: "))
repetir(t,n)