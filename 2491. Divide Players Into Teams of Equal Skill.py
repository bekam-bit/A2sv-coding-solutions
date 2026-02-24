class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
       
        n = len(skill)
        left = 0
        right = n - 1

        total_sum = 0
        k = skill[0] + skill[-1]

        while left <= right:
            if skill[left] + skill[right] == k:
                total_sum += (skill[left] * skill[right])
            else:
                return -1
            left += 1
            right -= 1
        
        return total_sum 
