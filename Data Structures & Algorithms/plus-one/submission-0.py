class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        combined = [int("".join(map(str, digits)))+1]

        result = [int(digit) for digit in str(combined[0])] 

        return result
        