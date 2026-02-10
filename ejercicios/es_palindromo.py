def es_palindromo(texto):
    # 1. Convertimos a minúsculas y eliminamos espacios en blanco
    texto_limpio = texto.lower().replace(" ", "")

    # 2. Comparamos el texto original limpio con su versión invertida
    return texto_limpio == texto_limpio[::-1]


# Pruebas
print(es_palindromo("Radar"))           # True
print(es_palindromo("Python"))          # False
print(es_palindromo("Anita lava la tina"))  # True
