class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(len(nums)//2):
            freq = nums[2*i]
            value = nums[2*i+1]
            r = r+[value]*freq

        return r