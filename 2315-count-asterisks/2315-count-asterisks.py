class Solution:
    def countAsterisks(self, s: str) -> int:
        bars = 0
        count = 0

        for ch in s:
            if ch == '|':
                bars += 1
            elif ch == '*' and bars % 2 == 0:
                count += 1

        return count