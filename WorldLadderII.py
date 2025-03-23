class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict) 
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]

if __name__ == "__main__":
    sol = Solution()

    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(sol.wordBreak(s1, wordDict1))  # True

    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(sol.wordBreak(s2, wordDict2))  # True

    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s3, wordDict3))  # False
