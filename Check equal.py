class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        # dict={}
        a.sort()
        b.sort()
        
        i=0
        n1=len(a)
        n2=len(b)
        
        if n1 != n2:
            return
        
        for i in range(n1):
            if a[i] != b[i]:
                return False
        return True
        
        
                
