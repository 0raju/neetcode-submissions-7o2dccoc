class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        reverse = ""

        for c in s:
            if c.isalnum():
                reverse += c
        reverse = reverse.lower()

        return reverse == reverse[::-1]


        