class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points,key= lambda x : x[1])
        
        min_arrow=0
        
        i=0
        while i < len(sorted_points):
            
            xend = sorted_points[i][1]
            min_arrow += 1

            while i < len(sorted_points) - 1 and xend <= sorted_points[i+1][1] and xend >= sorted_points[i+1][0]:
                    i += 1
            
            i += 1
            
        return min_arrow 

          
                
            
            
            

            





