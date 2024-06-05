animal = "  chanCHito feliz  "
print(animal.upper())
print(animal.lower())
print(animal.capitalize()) #pone primer letra en mayuscula
print(animal.title())#pone en mayuscula primer letra de cada palabra
print(animal.strip())#quita espacios en blanco de los extremos
print(animal.strip().capitalize())
print(animal.lstrip())#quita espacios en blanco a la izquierda
print(animal.rstrip())#quita espacios en blanco a la derecha
print(animal.find('CH'))#busca un string y regresa su indice
print(animal.find('cH'))#sino encuentra el string regresa -1
print(animal.replace("nCH","j"))
print("nCH" in animal)#regresa True o False si encuentra o no la cadena
print("nCH" not in animal)#regresa True o False si encuentra o no la cadena

