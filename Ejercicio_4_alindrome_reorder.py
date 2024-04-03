def palindrome_reorder(S):
    N = len(S)
    resultado = [' '] * N

    
    frecuencia = {}
    for caracter in S:
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1

    contador = 0
    for value in frecuencia.values():
        if value % 2 != 0:
            contador += 1
    if contador > 1:
        return "NO SOLUTION"

    izq, der = 0, N - 1
    for caracter in frecuencia:
        if frecuencia[caracter] % 2 == 1:
            resultado[N // 2] = caracter
            frecuencia[caracter] -= 1
        while frecuencia[caracter] > 0:
            resultado[izq] = resultado[der] = caracter
            izq += 1
            der -= 1
            frecuencia[caracter] -= 2

    return ''.join(resultado)
S = "rreeccoon"
print(palindrome_reorder(S))
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
