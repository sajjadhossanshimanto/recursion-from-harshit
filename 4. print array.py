def print_list(l: list, index=0):
    if index==len(l):
        return

    print(l[index])
    print_list(l, index+1)

print_list([1, 2, 3, 4, 5])