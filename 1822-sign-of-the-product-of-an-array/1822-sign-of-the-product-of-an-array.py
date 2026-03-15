class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            if num == 0:
                return 0
            product *= num
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0