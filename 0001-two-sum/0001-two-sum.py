class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=0
        l=len(nums)
        for i in range(l):
           for j in range(i+1,l):
            sum=nums[i]+nums[j]
            if (sum==target):
                return [i,j]
