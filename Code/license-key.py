   s = s.replace("-","").upper()
        result = []
        while len(s) > k:
            result.append(s[-k:])
            s = s[:-k]
        result.append(s)
        return "-".join(result[::-1])
