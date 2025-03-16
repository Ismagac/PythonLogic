class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):
                return i == len(s)
            
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                memo[(i, j)] = first_match and dp(i + 1, j + 1)
            
            return memo[(i, j)]
        
        return dp(0, 0)
        
solution = Solution()
print(solution.isMatch("aa", "a"))    # False
print(solution.isMatch("aa", "a*"))   # True
print(solution.isMatch("ab", ".*"))   # True
print(solution.isMatch("aab", "c*a*b")) # True
