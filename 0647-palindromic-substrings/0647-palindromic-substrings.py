class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                substring = s[i : j+1]
                if substring == substring[::-1]:
                    c=c+1
        return c