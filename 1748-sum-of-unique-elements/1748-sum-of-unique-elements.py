class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        s=0
        for num in nums:
            if num in freq:
                freq[num] = freq.get(num,0)+1
            else:
                freq[num] = 1
        for num in nums:
            if freq[num] == 1:
                s+=num
        return s