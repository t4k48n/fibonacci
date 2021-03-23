def fibonacci(n):
    if n in fibonacci.memo:
        return fibonacci.memo[n]
    if n <= 1:
        fibonacci.memo[n] = n
        return fibonacci.memo[n]
    fibonacci.memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci.memo[n]
fibonacci.memo = {}

def fibonacci_list(n):
    return [fibonacci(i) for i in range(0, n + 1)]

N = 10

# 0からNまでのフィボナッチ数列を表示．
for i in range(N + 1):
    print(fibonacci(i))

print(fibonacci_list(10))
