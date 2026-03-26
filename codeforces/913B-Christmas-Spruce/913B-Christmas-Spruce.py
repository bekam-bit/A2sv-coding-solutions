def dfs(start):
    cnt = 0

    if not Tree[start]:
        return True
    
    for v in Tree[start]:
        if not Tree[v-1]:
            cnt += 1
        else:
            if not dfs(v - 1):
                return False

    if cnt < 3:
        return False
    return True

print("No" if not dfs(0) else "Yes")