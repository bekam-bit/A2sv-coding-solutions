class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
      
        h = 0 
        for i in range(len(citations)):
            if citations[i] > i:
                h = i+1
            else:
                break
                
        return h
        
