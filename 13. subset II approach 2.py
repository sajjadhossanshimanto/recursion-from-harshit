

# with for loop
all_sub = []
def subsets(l, index=0, temp = []):
    '''sorting is must before passing to the function'''
    
    all_sub.append(temp[:])
    
    prev = None
    for i in range(index, len(l)):
        if prev == l[i]: continue
        prev = l[i]
        # single line condition without extra variable
        # if i>index and l[i]==l[i-1]: continue

        temp.append(l[i])
        subsets(l, i+1, temp)
        temp.pop()



l = ['a', 'b', 'b', 'c']
s.sort()
subsets(l)
print(all_sub)
