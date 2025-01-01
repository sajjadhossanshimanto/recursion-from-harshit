

def print_Nto1(n):
    if n==0:
        return
    
    print(n, end=" ")
    print_Nto1(n-1)

print_Nto1(10)