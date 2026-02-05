class Solution:    
    def findUnion(self, a, b):
        # code here
        
        res=[]
        n1=len(a)
        n2=len(b)
        
        seen=set()
        i=0
        j=0
        
        while i<n1 and j<n2:
            
            if a[i] not in seen:
                res.append(a[i])
                seen.add(a[i])
                
            if b[j] not in seen:
                res.append(b[j])
                seen.add(b[j])
            i+=1
            j+=1
                
        while i<n1: 
            if a[i] not in seen:
                res.append(a[i])
                seen.add(a[i])
            i+=1
            
        while j<n2: 
            if b[j] not in seen:
                res.append(b[j])
                seen.add(b[j])
            j+=1
            
        res.sort()
        return res
            
            
