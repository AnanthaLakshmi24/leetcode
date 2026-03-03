class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n
        while True:
            binary = bin(x)[2:]  
            if all(ch == '1' for ch in binary):
                return x
            
            x += 1