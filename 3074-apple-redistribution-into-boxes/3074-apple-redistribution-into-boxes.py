class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        count = 0
        total = 0
        capacity.sort(reverse=True)

        for c in capacity:
            total += c
            count += 1
            if total>=total_apples:
                return count
            