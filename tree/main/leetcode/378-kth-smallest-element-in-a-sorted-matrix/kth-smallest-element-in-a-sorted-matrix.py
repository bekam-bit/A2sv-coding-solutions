class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap=[]
        visited=set()

        init=matrix[0][0]
        heapq.heappush(min_heap,(matrix[0][0],0,0))
        visited.add((0,0))

        n=len(matrix)
       
        def is_valid(r,c):
            return 0 <=r < n and 0 <= c <n

        kth_smallest_value= -1
        for _ in range(k):
            if not min_heap:
                break
            val, r, c = heapq.heappop(min_heap)
            kth_smallest_value = val

            next_r1, next_c1 = r, c + 1
            next_r2, next_c2 = r + 1, c

            if is_valid(next_r1, next_c1) and (next_r1, next_c1) not in visited:
                heapq.heappush(min_heap, (matrix[next_r1][next_c1], next_r1, next_c1))
                visited.add((next_r1, next_c1))
            
            if is_valid(next_r2, next_c2) and (next_r2, next_c2) not in visited:
                heapq.heappush(min_heap, (matrix[next_r2][next_c2], next_r2, next_c2))
                visited.add((next_r2, next_c2))
        
        return kth_smallest_value