num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))

resul = 0
for num in range(num1,num2+1):
    resul += num
print(f'La suma es {resul}')
