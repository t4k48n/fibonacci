n1 = 0
n2 = 1

N = 10

# 0からNまでのフィボナッチ数列を表示．
for i in range(N + 1):
    if i == 0:
        print(n1)
    elif i == 1:
        print(n2)
    else:
        n_ = n1
        n1 = n2
        n2 = n2 + n_
        print(n2)
