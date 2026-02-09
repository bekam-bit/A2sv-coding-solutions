class RandomizedSet:

    def __init__(self):
       self.rand_list=[]
    
    def insert(self, val: int) -> bool:
        if val not in self.rand_list:
            self.rand_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.rand_list:
            self.rand_list.remove(val)
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
