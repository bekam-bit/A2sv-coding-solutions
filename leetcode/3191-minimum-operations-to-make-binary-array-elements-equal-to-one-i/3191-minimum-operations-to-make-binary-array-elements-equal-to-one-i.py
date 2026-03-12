class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque(nums[:3])

        min_op = 0

        if queue[0] == 0:
            for i in range(3):
                queue[i] ^= 1
            min_op += 1
        
        for i in range(3, n):
            queue.append(nums[i])
            queue.popleft()

            if queue and queue[0] == 0:
                for j in range(3):
                    queue[j] ^= 1
                min_op += 1
        
        return -1 if queue.count(0) > 0 else min_op
        
