class Solution:
    def reverseDegree(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            c = s[i].lower()
            rev = 26 - (ord(c)-ord('a'))
            tot += rev * (i+1)
        return tot