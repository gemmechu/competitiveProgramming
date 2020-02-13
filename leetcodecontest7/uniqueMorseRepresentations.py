from typing import List




class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def getMorse(param:str)->str:
            result=""
            for j in range(len(param)):
                index=ord(param[j])-97
                result+=morseCode[index]
            return result
        mydict={"":0}
        result=0
        for i in range(len(words)):
            morseResult=getMorse(words[i])
            if(mydict.get(morseResult) !=None):
                continue
            else:
                mydict[morseResult]=1
        result= len(mydict)-1
        return result
main=Solution()
words = ["gin", "zen", "gig", "msg"]
print(main.uniqueMorseRepresentations(words))