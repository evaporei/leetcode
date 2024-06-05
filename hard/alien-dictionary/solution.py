class Solution:
    def alienDictionary(self, words: List[str]) -> str:
        # unfortunatelly we can't use defaultdict(set)
        graph = { ch: set() for word in words for ch in word }
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ''
            offset = 0
            while offset < min_len:
                if word1[offset] != word2[offset]:
                    graph[word1[offset]].add(word2[offset])
                    break
                else:
                    offset += 1
        visited = {}
        res = []
        def dfs(ch: str) -> bool:
            if ch in visited:
                return visited[ch]
            visited[ch] = True
            for neighbor in graph[ch]:
                if dfs(neighbor):
                    return True
            visited[ch] = False
            res.append(ch)

        # keys
        for ch in graph:
            if dfs(ch):
                return ''

        res.reverse()
        return ''.join(res)

