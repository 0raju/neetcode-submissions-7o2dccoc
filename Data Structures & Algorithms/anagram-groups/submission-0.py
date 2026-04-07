class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram[sorted_s].append(s)
        return anagram.values()
        