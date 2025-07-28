class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            comp = target - numbers[i]
            # Avoid checking the same index and check for presence
            if comp in numbers[i+1:]:  # Only look forward to avoid reusing elements
                idx = numbers.index(comp, i+1)
                return [i+1, idx+1]
        return []
