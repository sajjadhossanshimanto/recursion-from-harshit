

def fibo(n):
    if n==0: return 0
    if n==1: return 1

    return fibo(n-1) + fibo(n-2)


print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))