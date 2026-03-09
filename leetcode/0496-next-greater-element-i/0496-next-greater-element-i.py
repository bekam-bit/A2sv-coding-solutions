class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = defaultdict(lambda: -1)

        for num in nums2:
            if not stack:
                stack.append(num)
            
            else:
                while stack and stack[-1] < num:
                    greater[stack[-1]] = num
                    stack.pop()
                
                stack.append(num)
        
        res = [greater[num] for num in nums1]

        return res