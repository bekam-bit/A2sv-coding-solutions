class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left = 0
        right = n - 1  

        numBoat = 0
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            numBoat += 1
        
        return numBoat + 1 if left == right else numBoat

        
            

           
