def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

N = 10

# 0からNまでのフィボナッチ数列を表示．
for i in range(N + 1):
    print(fibonacci(i))
