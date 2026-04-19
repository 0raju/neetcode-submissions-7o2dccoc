class Solution:
    def compress(self, chars: List[str]) -> int:
        
        comp = []

        left = 0
        right = 1

        count = 1
        while right < len(chars):
            if chars[left] == chars[right]:
                count+=1
            else:
                comp.append(chars[left])
                if count > 1:
                    comp += list(str(count))
                left = right
                count=1
            right+=1

        comp.append(chars[left])
        if count > 1:
            comp += list(str(count))
        
        for i, (val1, val2) in enumerate(zip(chars, comp)):
            chars[i] = comp[i]

        return len(comp)

