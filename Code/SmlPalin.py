def makeSmallestPalindrome(self, s: str) -> str:
    s = list(s)
    start = 0
    end = len(s)-1

    while start < end :
        if s[start] != s[end]:
            min_char = min(s[start],s[end])
            s[start] = min_char 
            s[end] = min_char 
        start += 1
        end -= 1
        
    return "".join(s)