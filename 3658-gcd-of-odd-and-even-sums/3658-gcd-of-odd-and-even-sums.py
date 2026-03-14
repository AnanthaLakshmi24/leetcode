class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        e=o=0
        for i in range(1,n*2):
            if i%2==0:
                e += i
            else:
                o += i
        return gcd(e,o)