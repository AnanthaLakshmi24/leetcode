class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = []
        for i in range(len(names)):
            people.append((heights[i], names[i]))
        people.sort(reverse=True)
        result = []
        for h, n in people:
            result.append(n)

        return result