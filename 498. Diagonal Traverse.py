class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_dict=defaultdict(list)
        
        row_len=len(mat)
        col_len=len(mat[0])

        res=[]

        for row in range(row_len):
            for col in range(col_len):
                diagonal_dict[row + col].append((row,col))
        
        for Sum, idxs in diagonal_dict.items():
            
            if Sum % 2 == 0:
                idxs.sort(key = lambda x : x[1])

            for r,c in idxs:
                res.append(mat[r][c])
                
        return res
       
