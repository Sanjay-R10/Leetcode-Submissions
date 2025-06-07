   l = 0
        r = 0
        curr_sum = 0
        max_sum = 0
        seen = set()

        while r < len(nums):
            while nums[r] in seen:
…                curr_sum -= nums[l]
                l += 1

            r += 1
        
        return max_sum