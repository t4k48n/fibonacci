def fibonacci(n):
    """ フィボナッチ数列のn番目を計算する．

    定義:
        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(2) = fibonacci(n - 1) + fibonacci(n - 2)
        ただし，n >=0
    """
    if n in fibonacci.memo:
        return fibonacci.memo[n]
    if n <= 1:
        fibonacci.memo[n] = n
        return fibonacci.memo[n]
    fibonacci.memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci.memo[n]
fibonacci.memo = {}

def fibonacci_list(n):
    """ フィボナッチ数列のn番目までを計算してリストに格納して返す．
    フィボナッチ数列の定義はfibonacci()関数に準拠．
    """
    return [fibonacci(i) for i in range(0, n + 1)]

N = 10

# 0からNまでのフィボナッチ数列を表示．
for i in range(N + 1):
    print(fibonacci(i))

print(fibonacci_list(10))
