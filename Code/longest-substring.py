def isNice(start,end):
        chars = set(s[start : end])
        for ch in chars :
             if ch.swapcase() not in chars :
                return False
        return True 

        max_len = 0
            res = ""

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if isNice(i,j) and j - i > max_len :
            max_len = j-i
            res = s[i : j]
        return res      