class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        s = list(s)

        old_score = 1
        new_score = 1
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])

            else:
                new_score = 1

                while stack and stack[-1] != "(":
                    while len(stack) >= 2 and isinstance(stack[-1], int) and isinstance(stack[-2], int):
                        prev = stack.pop()
                        stack.append(stack.pop() + prev)

                    else:
                        if isinstance(stack[-1], int):
                            old_score = stack.pop()
                            new_score = old_score * 2
                        
                if stack and stack[-1] == "(":
                    stack.pop()
                   
                stack.append(new_score)
                
        return sum(x for x in stack if isinstance(x, int))