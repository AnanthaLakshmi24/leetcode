class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # freq={}
        # n = len(nums)
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # for num, count in freq.items():
        #     if count == len(nums)//2:
        #         return num
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)