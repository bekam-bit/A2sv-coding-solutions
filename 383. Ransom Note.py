class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict=defaultdict(int)
        magazine_dict=defaultdict(int)

        for ransom in ransomNote:
            ransom_dict[ransom] += 1
        
        for maga in magazine:
            magazine_dict[maga] += 1
        
        for letter, cnt in ransom_dict.items():
            if letter not in magazine_dict:
                return False
            if letter in magazine_dict and ransom_dict[letter] > magazine_dict[letter]:
                return False
                
        
        return True

