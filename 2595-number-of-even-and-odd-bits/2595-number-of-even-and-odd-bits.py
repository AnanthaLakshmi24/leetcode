class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        num = bin(n)[2:][::-1]
        odd = 0
        even = 0
        for i, val in enumerate(num):
            if val == "1":
                if i% 2==0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]