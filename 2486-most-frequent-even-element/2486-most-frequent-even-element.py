class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num%2==0:
                if num in freq:
                    freq[num] +=1
                else:
                    freq[num] = 1 
        if not freq:
            return -1
        max_count = 0
        result = 0
        for num in freq:
            if freq[num]>max_count or (freq[num] == max_count and num <result):
                max_count = freq[num]
                result = num
        return result
            