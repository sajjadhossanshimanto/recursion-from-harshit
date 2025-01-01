

def fibo(n):
    if n==0: return 0
    if n==1: return 1

    return fibo(n-1) + fibo(n-2)

# for single call visualise with `stack`
# for multiple calls diagram appears tobe `tree`

print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))