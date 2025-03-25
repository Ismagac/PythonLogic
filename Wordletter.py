from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in wordSet:
                        queue.append((newWord, length + 1))
                        wordSet.remove(newWord)

        return 0

sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Salida: 5
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # Salida: 0
