#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo 
#si la división es exacta o no

print('Ingrese el primer numero: ')
num1 = int(input())
print('Ingrese el segundo numero: ')
num2 = int(input())
residuo = num1 % num2
if num1 == 0:
    print('No se puede dividir por 0')
else:
    if 0 == residuo:
        print('La division es exacta')

    else:
        print('La divsion no es exacta')
