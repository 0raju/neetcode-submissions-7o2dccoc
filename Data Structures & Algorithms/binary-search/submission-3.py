class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target not in nums: #option-1
        #     return -1
        # else:
        #     return nums.index(target)

        # binary search O(log n)

        left  = 0
        right = len(nums) - 1

        while left<=right:
            mid = left + ((right-left) //2)
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1



        