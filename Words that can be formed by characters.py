from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq_chars=Counter(chars)

        good_len=0
        
        for word in words:
            existed=True
            word_cnt = Counter(word)
           
            for c,cnt in word_cnt.items():
                if freq_chars[c] < cnt:
                    existed = False
                    break 
            
            if existed:
                good_len += len(word)
                

        return good_len
