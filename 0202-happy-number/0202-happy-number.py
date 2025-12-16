class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            if n == 1 or n == 7:
                return True
            if n < 10:
                return False

            sum = 0
            while n > 0:
                temp = n % 10
                sum += temp * temp
                n = n // 10

            n = sum