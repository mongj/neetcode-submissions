class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        def searchFrom(i: int, node: TrieNode) -> bool:
            curr_node = node
            for j in range(i, len(word)):
                if word[j] == '.':
                    for node in curr_node.children.values():
                        if searchFrom(j + 1, node):
                            return True
                    return False
                elif word[j] in curr_node.children:
                    curr_node = curr_node.children[word[j]]
                else:
                    return False
            return curr_node.is_end
            
        return searchFrom(0, self.root)

