class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        
        n = len(haystack)
        n1 = len(needle)
        
        while i < n:
            if haystack[i:i+n1] == needle:
                return i

            else:
                i += 1
                
        return -1
            
            
