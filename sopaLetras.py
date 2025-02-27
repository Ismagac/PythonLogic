from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} 
        self.word = None 

class Trie:
    def __init__(self):
        self.root = TrieNode()  

    def insert(self, word: str):
        node = self.root  
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  
            node = node.children[char] 
        node.word = word 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie() 
        for word in words:
            trie.insert(word)  

        rows, cols = len(board), len(board[0]) 
        result = []  

        def dfs(r, c, node):
            char = board[r][c] 
            if char not in node.children:
                return
            
            node = node.children[char] 
            if node.word:  
                result.append(node.word)
                node.word = None 

            board[r][c] = "#" 

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, node)

            board[r][c] = char 

        for r in range(rows):  
            for c in range(cols):
                dfs(r, c, trie.root)

        return result  



solution = Solution()

board1 = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words1 = ["oath", "pea", "eat", "rain"]
print(solution.findWords(board1, words1)) 
