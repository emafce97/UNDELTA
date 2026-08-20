class ValorIncorrectoEx(Exception):

    def __init__(self):
        super().__init__("[ERROR] El numero ingresado es incorrecto")

def ejercicio1(importe_vendido):
    sueldo_base = 450000
    comision = 0.08
    return sueldo_base + (comision * importe_vendido)

def ejercicio2():
    nota_uno = int(input("Ingrese la nota del primer parcial: "))
    if nota_uno < 0:
        raise ValorIncorrectoEx()
    nota_dos = int(input("Ingrese la nota del segundo parcial: "))
    nota_tres = int(input("Ingrese la nota del tercer parcial: "))
    promedio = (nota_uno + nota_dos + nota_tres) / 3
    print(f"El promedio del alumno es: {promedio}")

def ejercicio3():
    millas = int(input("Ingrese una distancia en millas: "))
    millas_a_kilometros = millas * 1.60934
    print(f"La distancia ingresada en millas equivale a {millas_a_kilometros} kms")

def ejercicio4():
    base = int(input("Ingrese la medida de la altura del rectangulo: "))
    altura = int(input("Ahora la medida de la base: "))
    area = base * altura
    perimetro = (base + altura) * 2
    print(f"El rectangulo tiene un area de {area} cm2, y un perimetro de {perimetro} cms")

def ejercicio5():
    monto_herencia = int(input("Ingrese el monto de la herencia: "))
    primer_hno = monto_herencia * 0.5
    segundo_hno = monto_herencia * 0.3
    tercer_hno = monto_herencia * 0.2
    print(f"El primer hermano va cobrar ${primer_hno}, el segundo hermano ${segundo_hno} y el tercero ${tercer_hno}")

def ejercicio6():
    grados = float(input("Ingrese la temperatura en grados centígrados: "))
    if grados < 0:
        clasificacion = "BAJO CERO"
    elif grados <= 25:
        clasificacion = "TEMPLADO"
    else:
        clasificacion = "CALUROSO"
    print(f"La temperatura ingresada se clasifica como: {clasificacion}")

def ejercicio7():
    monto_compra = float(input("Ingrese el monto de la compra: "))
    antiguedad = int(input("Ingrese la antiguedad del cliente: "))
    if antiguedad < 1:
        monto_a_pagar = monto_compra
    elif 1 <= antiguedad <= 3:
        monto_a_pagar = monto_compra * 0.95
    elif antiguedad > 3:
        monto_a_pagar = monto_compra * 0.90
    print(f"El cliente debera pagar ${monto_a_pagar} por tener {antiguedad} años de antiguedad")

def ejercicio8():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))
    aux = max(a, b)
    aux = max(aux, c)
    print(f"El numero mas grande es: {aux}")

def ejercicio9():
    edad = int(input("Ingrese una edad: "))
    categoria = None
    if 0 <= edad <= 5:
        categoria = "INFANTE"
    elif edad <= 12:
        categoria = "NIÑO/A"
    elif edad <= 17:
        categoria = "ADOLESCENTE"
    elif edad <= 64:
        categoria = "ADULTO"
    else:
        categoria = "ADULTO MAYOR"
    print(f"La edad ingresada corresponde a la categoria de {categoria}")

def ejercicio10():
    horas = int(input("Ingrese la cantidad de horas que el auto va estar estacionado: "))
    monto_a_pagar = None
    if horas < 1:
        monto_a_pagar = 500
    elif horas <= 3:
        monto_a_pagar = 800
    elif horas <= 6:
        monto_a_pagar = 1200
    else:
        monto_a_pagar = 1600
    print(f"El cliente debera pagar ${monto_a_pagar} por estacionares {horas}hs")

def ejercicio11():
    edad = int(input("Ingrese la edad: "))
    ingreso_mensual = float(input("Ingrese el ingreso mensual: "))
    score_crediticio = int(input("Ingrese el score crediticio: "))
    situacion = 18 <= edad <= 65 and ingreso_mensual >= 300000 and score_crediticio >= 700
    print(f"El cliente es apto para un credito? {situacion}")

def ejercicio12():
    monto = float(input("Ingrese el monto: "))
    es_internacional = True if int(input("Es una transaccion internacional? 1-Si 2-No: ")) == 1 else False
    hora_transaccion = int(input("Ingrese la hora en que se realizo la transaccion: "))
    alto_riesgo = monto >= 1000000 and es_internacional and 0 <= hora_transaccion <= 5
    if alto_riesgo:
        print("La transaccion es de RIESGO ALTO")
    else:
        print("La transaccion es de RIESGO NORMAL")

def ejercicio13():
    num = int(input("Ingrese un numero: "))
    for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

def ejercicio14():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    if a % 2 == 0:
        print(a, end = " ")
    for i in range(a + 1, b):
        if i % 2 == 0: print(i, end = " ") 
    if b % 2 == 0:
        print(b, end = "")

def ejercicio15():
    consumo_kwh = 0
    while (consumo_kwh >= 0):
        consumo_kwh = float(input("Ingrese el consumo energetico: "))
        if consumo_kwh <= 150:
            print("RESIDENCIAL T1")
        elif consumo_kwh <= 325:
            print("RESIDENCIAL T2")
        else:
            print("RESIDENCIAL T3")
    print("Se ingreso un valor incorrecto! Terminando el programa...")

def ejercicio16():
    numeros_ingresados = []
    suma = 0
    while True:
        numero = int(input("Ingrese un numero: "))
        numeros_ingresados.append(numero)
        if numero < 0:
            break
        suma += numero
    print(f"Se ingresaron los siguientes numeros: {numeros_ingresados}")
    print(f"La suma de los numeros positivos ingresados es: {suma}")

def ejercicio17():
    n = int(input("Ingrese la cantidad de edades que va cargar: "))
    suma = 0
    for i in range(n):
        edad = int(input("Ingrese una edad: "))
        suma = suma + edad
    print(f"El promedio de edad es de {int(suma / n)} años")

def ejercicio18():
    def factorial (num):
        if num < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado
    num = int(input("Ingrese un numero: "))
    factorial = factorial(num)
    print(f"El factorial de {num} es {factorial}")

def ejercicio19():
    max_temp = float('-inf')
    min_temp = float('inf')
    for i in range(20):
        temp = float(input("Ingrese una temperatura: "))
        max_temp = max(max_temp, temp)
        min_temp = min(min_temp, temp)
        print(f"Hasta el momento, la temperatura máxima ingresada es {max_temp}°, y la mínima es {min_temp}°")

def ejercicio20():
    notas = []
    suma = 0
    while True:
        nota = int(input("Ingrese una nota (o -1 para salir): "))
        if nota == -1:
            print("Saliendo...")
            break
        elif nota < 0 or nota > 10:
            print("[ERROR] Valor incorrecto")
        else:
            notas.append(nota)
            suma += nota
    if len(notas) == 0:
        print("No se ingresaron notas.")
    else:
        promedio = suma / len(notas)
        cant_aprobados = sum(1 for n in notas if n >= 4)
        print(f"El promedio de nota es: {promedio:.2f}.")
        print(f"La cantidad de alumnos aprobados es: {cant_aprobados}")


def ejercicio21():
    mediciones = [ 150, 220, 180, 300, 90, -1]
    mediciones_positivas = [i for i in mediciones if i >= 0]
    promedio_gral = sum(mediciones_positivas) / len(mediciones_positivas)
    mediciones_lentas = [i for i in mediciones_positivas if i > 200]
    porcentaje_medicioes_lentas = 100 * len(mediciones_lentas) / len(mediciones_positivas)
    print(f"Mediciones: {mediciones}")
    print(f"Promedio: {promedio_gral}")
    print(f"Lentas: {len(mediciones_lentas)} - Porcentaje: {porcentaje_medicioes_lentas} %")


def ejercicio22():
    error_actual = 100.0
    iteraciones = 0
    while error_actual >= 1.0:
        iteraciones += 1
        error_actual *= 0.85
        print(f"Iteración {iteraciones}: {error_actual:.2f}")    
    print(f"Se necesitaron {iteraciones} iteraciones para que el error actual sea menor que 1.0")


ejercicio2()
        
        