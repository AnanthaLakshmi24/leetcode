class Solution:
    def sumBase(self, n: int, k: int) -> int:
        store = []
        while n > 0:
            coff = n // k
            store.append(n%k)
            n = coff

        ans = 0
        for i in store:
            ans += i
        return ans