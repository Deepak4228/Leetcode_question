class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        trans = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            trans.append(row)
        return trans