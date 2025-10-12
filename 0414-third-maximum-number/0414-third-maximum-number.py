class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        k = list(set(nums))
        if len(k)>=3:
            k.sort()
            return k[-3]
        else:
            return max(nums)
            