class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        axis = Counter()
        total = 0
        for _, y, s in squares:
            area = s*s
            total += area
            axis[y] += s
            axis[y+s] -= s
        
        target = total / 2
        
        events = sorted(axis.items())
        cur = 0
        last_y = events[0][0] - 1
        for y, a_unit in events:
            dy = (y-last_y)
            nar = cur * dy
            if target - nar <= 0:
                return last_y + (target / nar) * dy

            target -= nar
            cur += a_unit
            last_y = y