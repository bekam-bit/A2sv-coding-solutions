class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ch_word={}
        word_ch={}
        words=s.split()
        
        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern,words):
            if ch in ch_word and ch_word[ch] != word:
                return False
            if word in word_ch and word_ch[word] != ch:
                return False
            
            ch_word[ch]=word
            word_ch[word]=ch
        
        return True
            

     
        
        
