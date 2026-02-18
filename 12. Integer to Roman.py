class Solution:
    def intToRoman(self, num: int) -> str:
        s_v_pair = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10 : "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C" ,
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M"
        }

        res=[]
        while num > 0:
            
            if len(str(num)) == 4:
                ans = num // 1000
                n = ans * 1000
                res.extend([s_v_pair[1000]] * ans)
                num -= n
            
            if len(str(num)) == 3:
                ans = num // 100
                n = ans * 100
                
                if n in s_v_pair:
                    res.extend(s_v_pair[n])

                if n > 500 and n not in s_v_pair:
                    res.extend(s_v_pair[500])
                    diff = n - 500
                    diff //= 100
                    res.extend([s_v_pair[100]] * diff)
               
                if n < 500 and n not in s_v_pair:
                    diff = n // 100
                    res.extend([s_v_pair[100]] * diff)
                
                num -= n
            
            if len(str(num)) == 2:
                ans = num // 10
                n = ans * 10

                if n in s_v_pair:
                    res.extend(s_v_pair[n])
                
                if n > 50 and n not in s_v_pair:
                    res.extend(s_v_pair[50])
                    diff = n - 50
                    diff //= 10
                    res.extend([s_v_pair[10]] * diff)
                
                if n < 50 and n not in s_v_pair:
                    diff = n // 10
                    res.extend([s_v_pair[10]] * diff)
                
                num -= n
            
            if len(str(num)) == 1:

                if num in s_v_pair:
                    res.extend(s_v_pair[num])
                
                if num > 5 and num not in s_v_pair:
                    res.extend(s_v_pair[5])
                    diff = num - 5
                    res.extend([s_v_pair[1]] * diff)
                
                if num < 5 and num not in s_v_pair:
                    diff = num // 1
                    res.extend([s_v_pair[1]] * diff)
                
                num //= 10
        
        return "".join(res)


