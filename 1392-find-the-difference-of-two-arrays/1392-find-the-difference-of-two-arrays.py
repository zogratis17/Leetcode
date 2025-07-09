class Solution:
    def findDifference(self, num1: List[int], num2: List[int]) -> List[List[int]]:
       set1,set2 = set(num1),set(num2)
       return [list(set1-set2), list(set2-set1)]