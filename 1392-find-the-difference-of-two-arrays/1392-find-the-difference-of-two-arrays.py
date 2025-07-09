class Solution:
    def findDifference(self, num1: List[int], num2: List[int]) -> List[List[int]]:
        dist1 = [] 
        dist2 = []
        set1,set2 = set(num1) , set(num2)

        for num in num2:
            if num not in set1:
                set1.add(num)
                dist1.append(num)
        for num in num1:
            if num not in set2:
                set2.add(num)
                dist2.append(num)
        
        return [dist2, dist1]