from collections import Counter
brackets = list(input())

stack = [-1]

max_len = 0
cur_len = 0
lengths = []

for idx, bracket in enumerate(brackets):
    if bracket == "(":
        stack.append(idx)
    
    else:
        stack.pop()
        if stack:
            cur_len = idx - stack[-1]
            lengths.append(cur_len)
            max_len = max(max_len, cur_len)
            
        else:
            stack.append(idx)


if max_len == 0:
    print(0,1)

else:
    count = lengths.count(max_len)
    print(max_len, count)