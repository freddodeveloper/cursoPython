# n1 = input("Ingresa primer numero: ")
# n2 = input("Ingresa segundo numero: ")

# print(n1, n2)
# print(n1 + n2)

# n1 = int(n1)
# n2 = int(n2)
# print(n1 + n2)

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese nùmero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break

    print(f"El resultado es {resultado}")
