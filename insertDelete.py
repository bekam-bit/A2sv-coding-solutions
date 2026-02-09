class RandomizedSet:

    def __init__(self):
        self.seen=set()
        self.rand_list=[]

    def insert(self, val: int) -> bool:
        if val not in self.seen:
            self.rand_list.append(val)
            self.seen.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.seen:
            self.rand_list.remove(val)
            self.seen.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.rand_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
