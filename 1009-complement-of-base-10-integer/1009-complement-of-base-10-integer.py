class Solution:
    def bitwiseComplement(self, n: int) -> int:
        k = bin(n)[2:]
        c = ""
        for b in k:
            if b=='0':
                c += '1'
            else:
                c+='0'
        return int(c,2)