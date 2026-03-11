class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)

        stack = []
        temp_stack = []
        for i in range(len(s)):
           

            if s[i] != "]":
                stack.append(s[i])

            elif s[i] == "]":
                temp_stack = []
                while stack and stack[-1] != "[":
                    temp_stack.append(stack.pop())
                
                
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k += stack.pop()
                
                k = int(k[::-1])

                decode_st = k * ("".join(temp_stack[::-1]))
                stack.append(decode_st)

        return "".join(stack)    
                
                    