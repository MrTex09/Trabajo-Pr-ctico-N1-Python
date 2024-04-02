def number_spiral(Y, X):
    
    if Y > X:       
        ans = (Y - 1) * (Y - 1)     
        if Y % 2 != 0:
            add = X
        else:
            add = 2 * Y - X
        return ans + add
    else:
        ans = (X - 1) * (X - 1)
        if X % 2 == 0:
            add = Y
        else:
            add = 2 * X - Y
        return ans + add
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
Y = 2
X = 2
print(number_spiral(Y, X))
