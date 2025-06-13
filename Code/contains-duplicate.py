    seen = set()
    r = 0
    l = 0
    n = len(nums)

    while r < n :
        if nums[r] in seen :
            return True
        seen.add(nums[r])

        if r-l >= k:
            seen.remove(nums[l])
            l += 1

        r += 1

    return False