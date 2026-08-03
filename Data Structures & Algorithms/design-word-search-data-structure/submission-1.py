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

    def searchFrom(self, word: str, node: TrieNode) -> bool:
        current_node = node
        for i in range(len(word)):
            if word[i] == ".":
                return any([self.searchFrom(word[i + 1:], node) for node in current_node.children.values()])
            elif word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                return False
        return current_node.is_end
    
    def search(self, word: str) -> bool:
        return self.searchFrom(word, self.trie)

