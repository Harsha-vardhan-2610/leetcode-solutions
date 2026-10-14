class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l = []

        for i in range(len(sentences)) :
            m = sentences[i].split(" ")
            c = len(m)
            l.append(c)
        
        return max(l)