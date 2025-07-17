class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            value = nums[i+1]
            result.extend([value]*freq)
        return result
