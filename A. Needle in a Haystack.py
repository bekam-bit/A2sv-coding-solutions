from collections import Counter

def ANeedleInAHatstack():
    tc = int(input())
    for _ in range(tc):
        s = list(input())
        t = list(input())

        s_cnt = Counter(s)
        t_cnt = Counter(t)

        for ch in s_cnt:
            if s_cnt[ch] > t_cnt[ch]:
                print("Impossible")
                break
        else:
            t_elem = []
            for ch in t_cnt:
                extra = t_cnt[ch] - s_cnt[ch]
                t_elem.extend([ch] * extra)
        
            t_elem.sort()
            
            res = []
            n = len(t_elem)
            n1 = len(s)
            
            i = 0
            j = 0
            if n > 0:
                
                while i < n and t_elem[i] < s[0]:
                    res.append(t_elem[i])
                    i += 1

                insert_before_equal = False
                for ch in s:
                    if ch != s[0]:
                        insert_before_equal = ch < s[0]
                        break

                if not insert_before_equal:
                    while i < n and t_elem[i] == s[0]:
                        res.append(t_elem[i])
                        i += 1
                
                while i < n and j < n1:
                    if s[j] <= t_elem[i]:
                        res.append(s[j])
                        j += 1
                    else:
                        res.append(t_elem[i])
                        i += 1

            else:
                res.extend(s)
                print("".join(res))
                continue

            while i < n:
                res.append(t_elem[i])
                i += 1
            
            while j < n1:
                res.append(s[j])
                j += 1
            
            print("".join(res))

ANeedleInAHatstack()
