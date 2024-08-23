# and, or, not

gas = True
encendido = True
edad = 18

if not gas and (encendido and edad >17):
    print('Puedes avanzar')

if gas or encendido or edad >17:
    print('Puedes avanzar')

if not gas or encendido:
    print('Puedes avanzar')