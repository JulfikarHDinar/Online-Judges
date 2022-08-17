class Solution:
    def wordToMorse(self, word):
        alphaMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        list1 = []
        for i in word:
            ascii = ord(i)  #ascii of the word. ascii of 'a' is 97
            list1.append(alphaMorse[ascii-97])
        list1 = ''.join(map(str, list1))
        #print(list1)
        return list1

    def uniqueMorseRepresentations(self, words):
        list1 = []
        for i in words:
            list1.append(self.wordToMorse(i))
        #print(list1)
        unique = set(list1)
        return len(unique)