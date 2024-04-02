def weird_algorithm(n):
    sequence = [n]
    while n != 1:
        if n % 2 != 0:
            n = n * 3 + 1
        else:
            n //= 2
        sequence.append(n)
    return sequence

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print(weird_algorithm(3))
