class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.queue = deque()
        self.cnt = defaultdict(int)
       
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.cnt[num] += 1

        if len(self.queue) > self.k:
            left_num = self.queue.popleft()
            self.cnt[left_num] -= 1

            if self.cnt[left_num] == 0:
                del self.cnt[left_num]

        return len(self.queue) == self.k and self.cnt[self.value] == self.k
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)