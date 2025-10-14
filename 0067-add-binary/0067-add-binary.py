class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a,2)+int(b,2))[2:]
        x = int(a, 2)
        y = int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]