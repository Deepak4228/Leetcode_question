class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result=list(words[0])
        for i in range(1,len(words)):
            temp=[]
            current=list(words[i])
            for ch in result:
                if ch in current:
                    temp.append(ch)
                    current.remove(ch)
            result=temp
        return result
        