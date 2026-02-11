class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # sorted_word1=sorted(word1)
        # sorted_word2=sorted(word2)

        counter1=Counter(word1)
        counter2=Counter(word2)

        if sorted(counter1.values()) != sorted(counter2.values()):
            return False

        if len(word1) != len(word2):
            return False 
            
        if set(counter1.keys()) != set(counter2.keys()):
            return False

        return True
