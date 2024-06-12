class Node:
    def __init__(self, final=False):
        self.children = [None] * 26
        self.final = final

def idx(char: str) -> int:
    return ord(char) - ord('a')

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            i = idx(char)
            if not curr.children[i]:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.final = True

    def search(self, word: str) -> bool:
        def dfs(j: int, node: Node) -> bool:
            curr = node
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in curr.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                index = idx(char)
                if not curr.children[index]:
                    return False
                curr = curr.children[index]
            return curr is not None and curr.final
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
