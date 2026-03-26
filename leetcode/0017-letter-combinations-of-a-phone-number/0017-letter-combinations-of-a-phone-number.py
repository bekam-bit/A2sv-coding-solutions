class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return

        self.digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        self.res = []
        self.digits = digits
        self.backTrack(0, "")
        return self.res

    def backTrack(self, idx, cur):
        if idx == len(self.digits):
            self.res.append(cur[:])
            return 
        
        for letters in self.digit_to_letters[self.digits[idx]]:
            self.backTrack(idx + 1, cur + letters)
            

