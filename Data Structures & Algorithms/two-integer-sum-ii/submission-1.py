# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]
#         return []

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}  # Store number and its index

        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_map:
                return [num_map[complement] + 1, i + 1]  # 1-based index
            num_map[num] = i

        return []