class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum= n*(n+1)//2
        c=0 
        for num in nums:
            c=c+num
        return sum-c