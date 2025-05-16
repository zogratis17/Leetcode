class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp=[1]*len(words)
        mem=[-1]*len(words)
        for i in range(len(words)-1,-1,-1):
            for j in range(i+1,len(words)):
                if groups[i]!=groups[j] and len(words[i])==len(words[j]):
                    dist=0
                    for k in range(len(words[i])):
                        if words[i][k]!=words[j][k]:
                            dist+=1
                        if dist>1:break
                    if dist==1:
                        if dp[j]+1>dp[i]:
                            dp[i]=dp[j]+1
                            mem[i]=j

        index=dp.index(max(dp))
        res = [words[index]]
        bool=True
        while bool:
            if mem[index]==-1:
                bool=False
            else:
                res.append(words[mem[index]])
            index=mem[index]
        return res