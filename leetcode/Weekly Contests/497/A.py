class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(matrix[i]) for i in range(len(matrix))]
    
    