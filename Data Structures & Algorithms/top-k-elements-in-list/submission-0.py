class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict()

        for num in nums:
            if num not in frequency.keys():
                frequency[num] = 1
            else:
                frequency[num] += 1
        array = sorted(frequency, key = frequency.get, reverse=True)

        return array[:k]
        