class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        for _ in range(4):
            
            if mat == target:
                return True
            
            for row in range(n):
                for col in range(row + 1, n):
                    mat[row][col], mat[col][row] = mat[col][row], mat[row][col]
            
            for row in range(n):
                mat[row].reverse()

        return False

               
