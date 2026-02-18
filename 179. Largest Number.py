class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_list=list(map(str,nums))
        
        def compare(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
            
        nums_list.sort(key=cmp_to_key(compare))

        res="".join(nums_list)
        
        return "0" if res[0] == "0" else res

