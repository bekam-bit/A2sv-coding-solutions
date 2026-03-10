class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for st in s:
            if st == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(st)
        
        return "".join(stack)

