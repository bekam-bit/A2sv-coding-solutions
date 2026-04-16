def isPossible(idx, b):
        low = 0
        high = m - 1
        res = b[-1]

        while low <= high:
            mid = (low + high) // 2
            if b[mid] - a[idx] >= a[idx - 1]:
                res = b[mid]
                high = mid - 1
            else:
                low = mid + 1

        return res 

    a[0] = min(a[0], b[0] - a[0])
    for i in range(1,n):
        ans = isPossible(i, b)
        if ans - a[i] < a[i-1] and a[i] < a[i-1]: 
                print("NO")
                break
        elif a[i] < a[i - 1]:
            a[i] = ans - a[i]
        elif ans - a[i] < a[i-1]:
            pass 
        else:
            a[i] = min(a[i], ans - a[i])
    else:
        print("YES")