class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = set()
        for num in nums:
            s.add(int(num,2))
        for i in range(2**n):
            if i not in s:
                return format(i,f'0{n}b')