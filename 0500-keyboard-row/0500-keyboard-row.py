class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set ('qwertyuiop')
        r2 = set ('asdfghjkl')
        r3 = set ('zxcvbnm')
        res=[]
        
        for word in words:
            lw = set(word.lower())

            if lw.issubset(r1) or lw.issubset(r2) or lw.issubset(r3):
                res.append(word)
        
        return res