class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # xorr = 0
        # for n in nums:
        #     xorr ^= n
        # return xorr

        # stack = []
        # for n in nums:
        #     if stack and stack[-1] == n:
        #         stack.pop()
        #     else:
        #         stack.append(n)

        # return stack[0]

        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
        