class TrieNode:

    def __init__(self, char: str, is_end: bool):
        self.char = char
        self.is_end = is_end
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode("ROOT", False)

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char, False)
            current_node = current_node.children[char]
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return current_node.is_end

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return True
        