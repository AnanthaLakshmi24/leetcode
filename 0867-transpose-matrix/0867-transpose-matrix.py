class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        result = []

        for j in range(n): 
            new_row = []
            for i in range(m):
                new_row.append(matrix[i][j])
            result.append(new_row)

        return result