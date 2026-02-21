class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        c = 0
        for i in range(left,right+1):
            k = bin(i)[2:]
            r = k.count('1')
            if is_prime(r):
                c+=1
        return c