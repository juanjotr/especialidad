''' Programa 5 '''
NUM = input("Introduce el primer numero para comparar: ")
NUM = int(NUM)
NUM2 = input("Introduce el segundo numero para comparar: ")
NUM2 = int(NUM2)
NUM3 = input("Introduce el tercer numero para comparar: ")
NUM3 = int(NUM3)
if NUM > NUM2:
    if NUM > NUM3:
        print("El numero A es el mayor")
    else:
        print("El numero C es el mayor")
else:
    if NUM2 > NUM3:
        print("El numero B es el mayor")
    else:
        print("El numero C es el mayor")
