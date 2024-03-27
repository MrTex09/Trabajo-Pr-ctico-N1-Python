def calcular_raiz_cuadrada(numero):
    assert numero >= 0, "El número debe ser positivo"
    return numero ** 0.5

resultado = calcular_raiz_cuadrada(9)
print(resultado)  # Output: 3.0

resultado = calcular_raiz_cuadrada(1)  # Genera AssertionError
