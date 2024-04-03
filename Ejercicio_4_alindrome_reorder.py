def palindrome_reorder(S):
    # Obtener la longitud de la cadena S
    N = len(S)
    # Inicializar una lista de resultado con espacios en blanco de longitud N
    resultado = [' '] * N
    frecuencia = {}
    for caracter in S:
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1

    # Contar cuántos caracteres tienen una frecuencia impar
    contador = 0
    for value in frecuencia.values():
        if value % 2 != 0:
            contador += 1
    # Si hay más de un carácter con frecuencia impar, no es posible formar un palíndromo
    if contador > 1:
        return "NO SOLUTION"

    # Definir los índices izquierdo y derecho para llenar la lista de resultado
    izq, der = 0, N - 1
    # Iterar sobre cada carácter y su frecuencia
    for caracter in frecuencia:
        # Si la frecuencia del carácter es impar, colocarlo en el medio de la lista de resultado
        if frecuencia[caracter] % 2 == 1:
            resultado[N // 2] = caracter
            frecuencia[caracter] -= 1
        # Llenar los caracteres restantes en ambos lados del palíndromo
        while frecuencia[caracter] > 0:
            resultado[izq] = resultado[der] = caracter
            izq += 1
            der -= 1
            frecuencia[caracter] -= 2
    return ''.join(resultado)
S = "aabbc"
print(palindrome_reorder(S))
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
