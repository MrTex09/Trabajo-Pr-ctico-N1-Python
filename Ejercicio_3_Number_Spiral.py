def number_spiral(Y, X):
    # Verifica si la coordenada Y es mayor que la coordenada X
    if Y > X:
        # Si Y es mayor que X, calcula el valor base de la espiral para la fila Y
        ans = (Y - 1) * (Y - 1)
        # Calcula el valor adicional a añadir al valor base
        if Y % 2 != 0:
            add = X
        else:
            add = 2 * Y - X
        # Devuelve la suma del valor base y el valor adicional
        return ans + add
    else:
        # Si X es mayor que o igual a Y, calcula el valor base de la espiral para la columna X
        ans = (X - 1) * (X - 1)
        # Calcula el valor adicional a añadir al valor base
        if X % 2 == 0:
            add = Y
        else:
            add = 2 * X - Y
        # Devuelve la suma del valor base y el valor adicional
        return ans + add
    
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
Y = 2
X = 2
print(number_spiral(Y, X))
