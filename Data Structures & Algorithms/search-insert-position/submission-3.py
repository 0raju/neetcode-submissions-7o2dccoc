class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        nums.append(target) # O(nlogn)
        nums = sorted(nums)
        return nums.index(target)
            
        # # binary search O(logn)
        # left, right  = 0, len(nums) - 1

        # while left<=right:
        #     mid = left + (right-left) //2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1

        # return left   