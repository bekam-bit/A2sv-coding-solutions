class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveDbill = 0
        tenDbill = 0

        for bill in bills:
            if bill == 5:
                fiveDbill += 1
            
            elif bill == 10:
                if fiveDbill == 0:
                    return False
                
                fiveDbill -= 1
                tenDbill += 1

            else:
                if fiveDbill  > 0 and tenDbill > 0:
                    fiveDbill -= 1
                    tenDbill -= 1
                
                elif tenDbill == 0 and fiveDbill >= 3:
                    fiveDbill -= 3
                
                else:
                    return False

        return True