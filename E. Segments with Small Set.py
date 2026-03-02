from collections import Counter

n, k = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
cur_cnt = 0
total_cnt = 0
cnt = Counter()

for right in range(n):
    cnt[nums[right]] += 1
    
    while left < n and len(cnt) > k:
        cnt[nums[left]] -= 1

        if cnt[nums[left]] == 0:
            del cnt[nums[left]]

        left += 1
      
    cur_cnt = right - left + 1
    total_cnt += cur_cnt
            
print(total_cnt)
