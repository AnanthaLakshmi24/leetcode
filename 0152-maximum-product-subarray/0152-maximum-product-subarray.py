class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxproduct = nums[0]
        n =len(nums)
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n-1-i]
            maxproduct = max(maxproduct,prefix,suffix)
            if prefix ==0:
                prefix = 1
            elif suffix ==0:
                suffix =1

        return maxproduct
            