def fibonacci(n):
    if n <= 0:
        return "Número inválido"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[-1]

n = int(input("Digite um número para encontrar o n-ésimo termo da série de Fibonacci: "))
print(f"O {n}-ésimo termo da série de Fibonacci é {fibonacci(n)}.")
