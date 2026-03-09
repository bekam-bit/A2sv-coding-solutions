class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_list = path.split("/")

        for dir in path_list:
            if dir == '' or dir == '.':
                continue
            
            elif dir == '..':
                if stack:
                    stack.pop()
                    
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
        



