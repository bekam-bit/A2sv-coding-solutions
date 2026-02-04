class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output=[]
        temp=[]
        in_block=False
        for src in source:
            i=0
            while i < len(src):
                if not in_block:
                    if src[i:i+2] == "//":
                        break
                    elif src[i:i+2] == "/*":
                        in_block=True
                        i+=1
                    else:
                        temp.append(src[i])
                else:
                    if src[i:i+2]=="*/":
                        in_block=False
                        i+=1
                i+=1
            if not in_block and temp:
                output.append("".join(temp))
                temp=[]
        return output
            
