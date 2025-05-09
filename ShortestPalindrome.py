class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)
        
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        
        to_add = rev[:len(s) - pi[-1]]
        return to_add + s

if __name__ == "__main__":
    sol = Solution()
    
    print("Testing shortestPalindrome method:")
    
    test1 = "aacecaaa"
    result1 = sol.shortestPalindrome(test1)
    print(f"Input: '{test1}' → Output: '{result1}'")
    
    test2 = "abcd"
    result2 = sol.shortestPalindrome(test2)
    print(f"Input: '{test2}' → Output: '{result2}'")
    

