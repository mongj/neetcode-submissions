class TrieNode:

    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode(None)

    def addWord(self, word: str) -> None:
        current_node = self.trie
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode(c)
            current_node = current_node.children[c]
        current_node.is_end = True
    
    def search(self, word: str) -> bool:
        def dfs(j: int, node: TrieNode) -> bool:
            current_node = node
            for i in range(j, len(word)):
                if word[i] == ".":
                    for node in current_node.children.values():
                        if dfs(i + 1, node):
                            return True
                    return False
                elif word[i] in current_node.children:
                    current_node = current_node.children[word[i]]
                else:
                    return False
            return current_node.is_end
        return dfs(0, self.trie)

