class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # keep going left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1  # keep going right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]

        # Time : O(log N)
        # Space : O(N)