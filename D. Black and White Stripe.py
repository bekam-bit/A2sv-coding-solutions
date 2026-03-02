tc = int(input())

for _ in range(tc):

    n, k = map(int, input().split())

    stripe = list(input())

    left = 0
    right = 0

    cur_cell = 0
    min_cell = float('inf')
    cnt_B = 0
    cnt_W = 0

    while right < n:
        while right < n and right - left < k:
            if stripe[right] == "B":
                cnt_B += 1
            else:
                cnt_W += 1
            
            right += 1
        
        cur_cell = k - cnt_B
        min_cell = min(min_cell,cur_cell)

        if stripe[left] == "B":
            cnt_B -= 1
        else:
            cnt_W -= 1

        left += 1

    print(min_cell)
        

    
        
