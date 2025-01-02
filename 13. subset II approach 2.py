

# with for loop
all_sub = []
def subsets(l, index=0, temp = []):
    all_sub.append(temp[:])
    
    prev = None
    for i in range(index, len(l)):
        if prev == l[i]: continue
        prev = l[i]

        temp.append(l[i])
        subsets(l, i+1, temp)
        temp.pop()



subsets(['a', 'b', 'b', 'c'])
print(all_sub)
