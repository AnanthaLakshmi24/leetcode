class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        k = bin(n)[2:]
        for i in range(1,len(k)):
            if k[i-1]==k[i]:
                return False
        return True