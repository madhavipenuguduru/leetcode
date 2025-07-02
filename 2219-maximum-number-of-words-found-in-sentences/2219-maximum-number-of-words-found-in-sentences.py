class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in sentences:
            temp=1
            for ch in i:
                if ch==" ":
                    temp+=1
            ans=max(ans,temp)
        return ans
            

        