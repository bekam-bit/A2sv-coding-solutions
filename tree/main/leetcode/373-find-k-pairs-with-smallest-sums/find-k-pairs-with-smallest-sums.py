class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        res_pairs = []
        visited = set()

        n = len(nums1)
        m = len(nums2)

        if not nums1 or not nums2 or k == 0:
            return []
        
        Sum = nums1[0] + nums2[0]
        heapq.heappush(min_heap, (Sum, 0, 0))
        visited.add((0, 0))

        while len(res_pairs) < k and min_heap:
            smallest_sum, i, j = heapq.heappop(min_heap)
            res_pairs.append([nums1[i], nums2[j]])

            if j + 1 < m and (i, j + 1) not in visited:
                s_Sum = nums1[i] + nums2[j + 1]
                heapq.heappush(min_heap, (s_Sum, i, j + 1))
                visited.add((i, j + 1))
            
            if i + 1 < n and (i + 1, j) not in visited:
                s_Sum = nums1[i + 1] + nums2[j]
                heapq.heappush(min_heap, (s_Sum, i + 1, j))
                visited.add((i + 1, j))
                
        return res_pairs