import random

opciones = ['piedra', 'papel','tijera']

pc = random.choice(opciones)

user = input('piedra, papel o tijera')
print(pc)

if user == pc:
    print('Empate')

elif user == 'piedra':
    if pc == 'papel':
        print('Pc gana!!')
    elif pc == 'tijera':
        print('Has ganado!!')

elif user == 'piedra':
    if pc == 'tijera':
        print('Has ganado!!')

elif user == 'papel':
    if pc == 'tijera':
        print('Pc gana!!')
    elif pc == 'piedra':
        print('Has ganado!!')

elif user == 'tijera':
    if pc == 'papel':
        print('Has ganado!!')
    elif pc == 'papel':
        print('Has ganado!!')

elif user == 'tijera':
    if pc == 'piedra':
        print('Pc gana!!')
    elif pc == 'papel':
        print('Has ganado')

