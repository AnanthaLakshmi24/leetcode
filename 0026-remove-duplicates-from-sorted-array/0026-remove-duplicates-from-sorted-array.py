class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for e in range(1, n):
            if nums[s] != nums[e]:
                s += 1
                nums[s] = nums[e]
        return s+1