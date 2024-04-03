def weird_algorithm(n):
    lista = [n]
    
    # Ejecutar el algoritmo mientras n no sea igual a 1
    while n != 1:
        if n % 2 != 0:
            n = n * 3 + 1
        else:
            n //= 2
        # Agregar el nuevo valor de n a la lista
        lista.append(n)
    return lista

# Comprobar si la función devuelve la secuencia esperada para el caso de prueba
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print(weird_algorithm(3))
