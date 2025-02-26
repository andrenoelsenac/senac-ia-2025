# O fatorial de um número é a multiplicação do número
# pelos anteriores até chegar em 1
# 5! = 5 * 4 * 3 * 2 * 1

# Ou podemos definir como:
# 
#  n! = 1, se n <= 1
#     = n * (n - 1)!, se n > 1

# def fatorial(n):
#     if n <= 1:
#         return 1
#     return n * fatorial(n - 1)

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat = fat * i
    return fat

numero = int(input('Digite um número: '))
print(f'{numero}! = {fatorial(numero)}')

