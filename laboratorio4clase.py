#LABORATORIO
#Usamos recursión con memoización para calcular números de Fibonacci
#MEMOS ES LA HABREBIATURA DE MEMORIZAR
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
# Calcular el número de Fibonacci de 50
resultado = fibonacci(50)
print("Fibonacci de 50 es:", resultado)
