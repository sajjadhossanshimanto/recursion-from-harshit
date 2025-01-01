

# def power(n, p):
#     if p==0: return 1
#     return n*power(n, p-1)

# print(power(3, 6))

def power(num, exp):# O(logN)
    if exp==0: return 1
    if exp==1: return num

    half = power(num, exp//2)
    if exp&1:# odd
        return half*half*num
    # even
    return half*half

print(power(2, 4))
print(power(3, 3))
print(power(3, 6))