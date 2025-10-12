class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        result = []
        for num in nums:
            freq[num]=freq.get(num,0)+1

        for num in freq:
            if freq[num]==2:
                result.append(num)

        return result