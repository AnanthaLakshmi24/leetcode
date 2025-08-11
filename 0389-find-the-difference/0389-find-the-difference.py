class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        s.append('0')
        t=sorted(t)
        for i in range(len(t)):
            if s[i]!=t[i]:
                return t[i]
        