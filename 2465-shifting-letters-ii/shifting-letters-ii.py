class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_list = list(s)
        pre_sum = [0] * (len(s_list) + 1)

        for i in range(len(shifts)):
            start, end , dir = shifts[i]
            val = 1 if dir == 1 else -1

            pre_sum[start] += val
            pre_sum[end + 1] -= val
        
        for i in range(1,len(s_list)):
            pre_sum[i] += pre_sum[i-1]

        new_char = [0] * (len(s_list))
        for j in range(len(s_list)):
            new_char[j] = chr(ord('a') + (ord(s_list[j]) - ord('a') + pre_sum[j]) % 26)
        
        return "".join(new_char)


            