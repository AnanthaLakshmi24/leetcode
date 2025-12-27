class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
        for num in range(1,10**6,1):
            if num not in freq:
                return num