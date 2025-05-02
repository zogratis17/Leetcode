class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'
        prev, result, n = 0, list(s), len(s)  
        for i in range(1, n):
            if s[i] == '.': continue
            if i - prev > 1:
                if s[prev] == s[i]:  # L....L OR R....R
                    for k in range(prev + 1, i):
                        result[k] = s[i]
                elif s[prev] == 'R' and s[i] == 'L': # RRLL
                    l, r = prev + 1, i - 1
                    while l < r:
                        result[l] = 'R'
                        result[r] = 'L'
                        l += 1
                        r -= 1
            prev = i

        return ''.join(result[1:-1])
        # Time:  O(n)
        # Space: O(1)