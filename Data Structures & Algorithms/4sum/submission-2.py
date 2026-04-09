class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n):
            fixed_1 = nums[i]
            # if fixed_1 > target:
            #         continue
            if i > 0 and nums[i] == nums[i-1]:
                    continue

            for j in range(i+1, n):
                fixed_2 = nums[j]
                # if fixed_2 > target or fixed_1+fixed_2>target:
                #     continue
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = n-1

                while left<right:
                    current_target = fixed_1 + fixed_2 + nums[left] + nums[right]
                    if current_target == target:
                        result.append([fixed_1, fixed_2, nums[left], nums[right]])
                        left+=1
                        right-=1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current_target>target:
                        right-=1
                    else:
                        left+=1
        
        return result





        