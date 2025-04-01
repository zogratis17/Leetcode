class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        up = down = right = left = 0

        for char in moves:
            if char=='U':
                up+=1
            elif char=='R':
                right+=1
            elif char=='L':
                left+=1
            elif char=='D':
                down+=1
        
        return up == down and right == left 