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
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            ch_ord = to_ord(char)
            if not curr.children[ch_ord]:
                curr.children[ch_ord] = Node()
            curr = curr.children[ch_ord]
        curr.final = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        res = set()

        def dfs(i: int, j: int, node: Node, word: str):
            if node.final:
                res.add(word)
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] == '#':
                return
            idx = to_ord(board[i][j])
            child = node.children[idx]
            if not child:
                return
            tmp = board[i][j]
            board[i][j] = '#'

            dfs(i - 1, j, child, word + tmp)
            dfs(i + 1, j, child, word + tmp)
            dfs(i, j - 1, child, word + tmp)
            dfs(i, j + 1, child, word + tmp)
            
            board[i][j] = tmp

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, "")

        return list(res)
