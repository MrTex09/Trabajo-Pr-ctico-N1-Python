def mis(n,l):    
    return  (n*((n +  1)) // 2) - sum(l)

assert mis(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print(mis(6, [1, 2, 4, 5]))