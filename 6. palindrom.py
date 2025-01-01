

def is_palindrom(s: str) -> bool:

    def recursive(l=0, r = len(s)-1):
        if r<l: return True

        if s[l]!=s[r]: return False
        return recursive(l+1, r-1)
    
    return recursive()


print(is_palindrom("abba"))
print(is_palindrom("abba1"))