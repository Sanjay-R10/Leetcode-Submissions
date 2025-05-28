class Solution:
    def replaceDigits(self, s: str) -> str:
        res =[]
        for i in range(len(s)):
            if i % 2 == 0:
                res.append(s[i])
            else:
                shift_char=chr(ord(s[i-1])+int(s[i]))
                res.append(shift_char)
            
        return"".join(res)