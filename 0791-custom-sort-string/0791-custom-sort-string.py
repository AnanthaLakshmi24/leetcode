class Solution:
    def customSortString(self, order: str, s: str) -> str:
       
        result = ""
        for ch in order:
            result += ch * s.count(ch)
        for ch in s:
            if ch not in order:
                result += ch
        return result
