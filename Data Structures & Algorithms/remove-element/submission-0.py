class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left +=1
        return left


        # temp = []
        # for n in nums:
        #     if n != val:
        #         temp.append(n)

        # for i in range(len(temp)):
        #     nums[i] = temp [i]

        # return len(temp)


        