def S(a, b):
    return a + b
def M(a, b):
    return a * b
def D(a,b):
    return a / b
def R(a,b):
    return a- b

while True:
    print("Menu principal ")
    print("1. Sumar")
    print("2. Multiplicar")
    print("3. Dividir")
    print("4. Restar")
    opc = input("Ingrese una opcion: ")
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    if opc=="1":
        print("la Suma es ",S(n1, n2))
    elif opc=="2":
        print("la Multiplicacion: ", M(n1, n2))
    elif opc=="3":
        print("la Division: ",D(n1, n2))
    elif opc=="4":
        print("la Resta es: ",R(n1, n2))
    else:
        print ("opcion invalida")
    
