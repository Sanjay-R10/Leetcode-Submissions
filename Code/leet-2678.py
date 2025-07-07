def fun(arr):
    count = 0
    for num in arr:
        age = int(num[11:13])
        if age > 60 :
            count += 1
    return count

print(fun(["7868190130M7522"]))