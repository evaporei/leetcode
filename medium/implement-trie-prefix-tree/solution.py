class Node:
    children: "List[Node | None]"
    final: bool

    def __init__(self, final=False):
        self.children = [None] * 26
        self.final = final

def to_ord(char: str) -> int:
    return ord(char) - ord('a')

class Trie:
    def __init__(self):
        self.entries = [Node() for i in range(26)]

    def insert(self, word: str) -> None:
        curr = self.entries[to_ord(word[0])]
        for char in word:
            ch_ord = to_ord(char)
            if not curr.children[ch_ord]:
                curr.children[ch_ord] = Node()
            curr = curr.children[ch_ord]
        curr.final = True

    def search(self, word: str) -> bool:
        curr = self.entries[to_ord(word[0])]
        for char in word:
            ch_ord = to_ord(char)
            if not curr.children[ch_ord]:
                return False
            curr = curr.children[ch_ord]
        return curr.final

    def startsWith(self, prefix: str) -> bool:
        curr = self.entries[to_ord(prefix[0])]
        for char in prefix:
            ch_ord = to_ord(char)
            if not curr.children[ch_ord]:
                return False
            curr = curr.children[ch_ord]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
