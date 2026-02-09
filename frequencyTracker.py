class FrequencyTracker:

    def __init__(self):
        
        self.tracker_dict=defaultdict(int)
        self.frequency=defaultdict(int)

    def add(self, number: int) -> None:
        prev = self.tracker_dict[number]
        curr = prev + 1
        self.tracker_dict[number] = curr
        self.frequency[curr] += 1
        self.frequency[prev] -= 1

    def deleteOne(self, number: int) -> None:
        if number in self.tracker_dict:
            prev = self.tracker_dict[number]
            curr = prev - 1
            self.tracker_dict[number] = curr
            self.frequency[curr] += 1
            self.frequency[prev] -= 1

            if self.tracker_dict[number] == 0:
                del self.tracker_dict[number]


    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
