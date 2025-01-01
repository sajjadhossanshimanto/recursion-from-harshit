

def begger(a: int, b: int) -> int:
    return a if a>b else b

def get_max(array, idx=0):
    if idx==len(array)-1:
        return array[idx]

    return begger(array[idx], get_max(array, idx+1))


print(get_max([2, 5, 9, 30]))