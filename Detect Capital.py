class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if (65 <= ord(word[0]) <= 90) and (65 <= ord(word[1]) <= 90):
            for char in word[2:]:
                if 65 > ord(char) or ord(char) > 90:
                    return False
            return True
        elif (97 <= ord(word[0]) <= 122) and (65 <= ord(word[1]) <= 90):
            return False
        else:
            for char in word[2:]:
                if 97 > ord(char) or ord(char) > 122:
                    return False
            return True