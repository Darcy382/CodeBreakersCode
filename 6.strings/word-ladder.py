from collections import defaultdict, deque
from typing import List

# O(N x M^2) time and space

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        # Make dict of all possible combinations for a certain mutation
        word_combos = defaultdict(list)
        for word in wordList:
            for i in range(L):
                word_combos[word[:i] + "*" + word[i + 1:]].append(word)

        visited = set()
        queue = deque([(beginWord, 1)])

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                for word in word_combos[current_word[:i] + "*" + current_word[i + 1:]]:
                    if word == endWord:
                        return level + 1
                    elif word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))

        return 0
