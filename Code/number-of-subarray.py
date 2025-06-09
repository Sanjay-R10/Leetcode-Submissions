    n = len(arr)
    l = 0
    curr_sum = 0
    count = 0
    target = k * threshold

    while l < k:
        curr_sum += arr[l]
    l += 1

        if curr_sum >= target:
            count +=1

        r = k

        while r < n :
            curr_sum += arr[r]
            curr_sum -= arr[r-k]

            if curr_sum >= target:
                count += 1

                r += 1

        return count
