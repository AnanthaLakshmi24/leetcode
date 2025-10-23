class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        first_k = words[:k]
        return " ".join(first_k)
