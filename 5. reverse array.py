
def reverse(array):
    def recursive(array, l=0, r = len(array)-1):
        if r<=l: return

        array[l], array[r] = array[r], array[l]
        recursive(array, l+1, r-1)

    recursive(array)


l = [34, 35, 37, 40]

print("before: ", l)
reverse(l)
print("after: ", l)
