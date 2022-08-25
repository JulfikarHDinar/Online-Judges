class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        str1 = "".join(map(str,word1))
        str2 = "".join(map(str,word2))

        if str1 == str2:
            return True
        else:
            return False
