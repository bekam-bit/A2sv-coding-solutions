class Solution:
    def isValid(self, s: str) -> bool:
        parenth = {")":"(", "}":"{", "]":"["}

        stack = []

        for st in s:
            if st in parenth.values():
                stack.append(st)

            else:
                if not stack or  stack[-1] != parenth[st]:
                     return False
                    
                stack.pop()

        return len(stack) == 0
                
