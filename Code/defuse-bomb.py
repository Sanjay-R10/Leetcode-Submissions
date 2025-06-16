    n = len(code)

        if k == 0:
            return[0]*n
        result = []
        code = code * 2 

        for i in range(n):
            if k > 0:
                window_sum = sum(code[i+1 : i+k+1])
            else:
                window_sum = sum(code[i+n+k : i+n])
            result.append(window_sum)
        return result