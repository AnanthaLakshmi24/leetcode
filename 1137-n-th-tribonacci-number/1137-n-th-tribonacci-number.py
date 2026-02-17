class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        left, middle, right = 0, 1, 1
        for i in range(3, n + 1):
            current = left + middle + right
            left = middle
            middle = right
            right = current
        return current