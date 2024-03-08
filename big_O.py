def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
 
    return soma
 
 
import timeit
print(timeit.timeit("soma1(10)", setup="from __main__ import soma1"))