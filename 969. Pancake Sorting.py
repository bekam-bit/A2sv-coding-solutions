class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        sorted_arr=sorted(arr,reverse=True)

        n=len(arr)
        res=[]
        i=0

        while n > 0:
            idx = arr.index(sorted_arr[i])
            k = idx + 1

            left = 0
            right = k

            if k > 0 and k < n:
                while left < right:
                    arr[left], arr[right - 1] = arr[right - 1], arr[left]
                    left += 1
                    right -= 1
                
                res.append(k)
            
            l=0
            r=n
            if k == 1:
                res.append(n)
                while l < r:
                    arr[l], arr[r - 1] = arr[r - 1], arr[l]
                    l += 1
                    r -= 1

            le=0
            rt=n
            id =  arr.index(sorted_arr[i])

            if id == 0:
                res.append(n)
                while le < rt:
                    arr[le], arr[rt - 1] = arr[rt - 1], arr[le]
                    le += 1
                    rt -= 1
            
            n -= 1
            i += 1
        
        return res
            
