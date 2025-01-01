

def power(n, p):
    if p==0: return 1
    return n*power(n, p-1)

print(power(2, 4))
print(power(3, 5))