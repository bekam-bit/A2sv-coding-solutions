class Solution:

    def canPlace(self, x, pos, n):
        prev_pos = pos[0]
        cnt = 1

        for i in range(1, len(pos)):
            cur_pos = pos[i]

            if cur_pos - prev_pos >= x:
                prev_pos = cur_pos
                cnt += 1
            
            if cnt == n:
                return True
        
        return False


    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high =  int(position[-1] / (m - 1.0)) + 1
        ans = 0

        while low <= high:
            mid = low + ((high - low) // 2)

            if self.canPlace(mid, position, m):
                ans = mid
                low = mid + 1
            
            else:
                high = mid - 1

        return ans


