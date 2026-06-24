class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        freq = Counter(words)
        max_heap = [(-cnt, word) for word, cnt in freq.items()]

        heapq.heapify(max_heap)

        for _ in range(k):
            _, word = heapq.heappop(max_heap)
            res.append(word)
        
        return res

