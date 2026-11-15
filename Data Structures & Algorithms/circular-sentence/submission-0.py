class Solution:
    # time -> O(n) space -> O(n)
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)

        for i in range(n):
            if words[i][-1] != words[(i+1)%n][0]:
                return False
        
        return True

    # time -> O(n) space -> O(1)
    # def isCircularSentence(sentence):
    #     if sentence[0] != sentence[-1]:
    #         return False

    #     for ch in range(len(sentence)):
    #         if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
    #             return False

    #     return True