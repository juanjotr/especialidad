''' Programa 4 '''
NUM = input("Introduce el primer numero para comparar: ")
NUM = int(NUM)
NUM2 = input("Introduce el segundo numero para comparar: ")
NUM2 = int(NUM2)
if NUM > NUM2:
    print("El numero A mayor que B")
elif NUM == NUM2:
    print("Los numeros A y B son iguales")
else:
    print("El numero B mayor que A")
