class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emp_map = {e.id: e for e in employees}

        queue = deque([id])
        total = 0

        while queue:
            curr_id = queue.popleft()
            emp = emp_map[curr_id]      
            total += emp.importance

            for sub_id in emp.subordinates:
                queue.append(sub_id)     

        return total