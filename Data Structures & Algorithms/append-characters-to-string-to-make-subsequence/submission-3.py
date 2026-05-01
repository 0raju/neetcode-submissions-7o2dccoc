class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        t_pointer = 0

        for char in s:
            if char == t[t_pointer]:
                t_pointer += 1
                if len(t) == t_pointer:
                    return 0
        
        return len(t) - t_pointer