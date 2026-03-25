class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.cur = []
        self.k = k
        self.n = n
        return self.backTrack(1)
    
    def backTrack(self, start):
        if len(self.cur) == self.k:
            self.res.append(self.cur[:])
            return
        
        for i in range(start, self.n + 1):
            self.cur.append(i)
            self.backTrack(i + 1)
            self.cur.pop()
        
        return self.res