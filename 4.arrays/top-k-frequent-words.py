def topKFrequent(self, words: List[str], k: int) -> List[str]:
    words = collections.Counter(words)
    words = list(words.items())
    words.sort(key=lambda x: (-x[1], x[0]))
    output = []
    for i in range(k):
        output.append(words[i][0])
    return output