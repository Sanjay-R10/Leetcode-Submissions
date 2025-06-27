def fun(jewels,stones):
    count = 0
    for char in stones:
        if char in jewels:
            count += 1
    return count
print(fun("aA","aAAbbbb"))