class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ones = min(numOnes, k)
        k -= ones
        zeros = min(numZeros, k)
        return ones - min(numNegOnes, k - zeros)