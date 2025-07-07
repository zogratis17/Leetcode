class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c=0
        freq = {'a':0,'b':0,'c':0}
        l = 0 

        for r in range(len(s)):
            freq[s[r]] += 1

            while all(freq[c]>0 for c in 'abc'):
                c += len(s) - r
                freq[s[l]] -=1
                l +=1
        
        return c

        # Time : O(N)
        # Space : O(1)