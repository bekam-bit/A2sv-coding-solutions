class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        min_cost = 0

        costs.sort(key = lambda x : x[0] - x[1])

        for i in range(n//2):
            min_cost += costs[i][0]
        
        for j in range(n//2, n):
            min_cost += costs[j][1]
        
        return min_cost