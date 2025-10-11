class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        m = n//2
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num in freq:
            if freq[num] >m:
                return num

            