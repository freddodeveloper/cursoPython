def limpiar_y_listar(texto):
    """
    Elimina espacios y devuelve una lista de caracteres.
    """
    return list(texto.replace(" ", ""))


def contar_caracteres(lista_caracteres):
    """
    Crea un diccionario con la frecuencia de cada caracter.
    """
    diccionario = {}
    for char in lista_caracteres:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1
    return diccionario


def ordenar_diccionario(diccionario):
    """
    Ordena el diccionario por valor (frecuencia) y devuelve una lista de tuplas.
    """
    return sorted(diccionario.items(), key=lambda x: x[1])


def obtener_mayores(lista_tuplas):
    """
    Filtra la lista para dejar solo los que tienen el valor máximo.
    """
    if not lista_tuplas:
        return []
    maximo_valor = max(lista_tuplas, key=lambda x: x[1])[1]

    resultado = [tupla for tupla in lista_tuplas if tupla[1] == maximo_valor]

    return resultado


def imprimir_resultado(lista_ganadores):
    """
    Imprime el mensaje con el formato solicitado.
    """
    if not lista_ganadores:
        print("No hay caracteres para mostrar.")
        return

    repeticiones = lista_ganadores[0][1]

    letras = [tupla[0].upper() for tupla in lista_ganadores]

    formato_letras = " * ".join(letras)

    print(
        f'Los caracteres que mas se repiten con "{repeticiones}" repeticiones son: * {formato_letras}')


# --- ENTRADA DE DATOS ---
string_entrada = "ab cdd c a"

# 1. Limpiar
lista_chars = limpiar_y_listar(string_entrada)
print(lista_chars)

# 2. Contar
diccionario_conteo = contar_caracteres(lista_chars)
print(diccionario_conteo)

# 3. Ordenar (convertir a tuplas)
lista_ordenada = ordenar_diccionario(diccionario_conteo)
print(lista_ordenada)

# 4. Filtrar los mayores
ganadores = obtener_mayores(lista_ordenada)

imprimir_resultado(ganadores)
