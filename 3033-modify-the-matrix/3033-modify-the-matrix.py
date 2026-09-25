class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == -1:
                    max_val = 0

                    for k in range(r):
                        if matrix[k][j] > max_val:
                            max_val = matrix[k][j]

                    matrix[i][j] = max_val

        return matrix