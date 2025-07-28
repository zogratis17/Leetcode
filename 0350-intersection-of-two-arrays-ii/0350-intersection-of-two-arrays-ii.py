class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        return list((Counter(a) & Counter(b)).elements())