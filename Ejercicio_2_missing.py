def mis(n, l):
    # Calcula la suma de los primeros 'n' números naturales usando la fórmula de la suma aritmética
    suma_total = (n * (n + 1)) // 2
    
    # Resta la suma de los elementos de la lista 'l' de la suma total calculada anteriormente
    diferencia = suma_total - sum(l)
    return diferencia
assert mis(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
print(mis(5, [1, 2, 4, 5]))
