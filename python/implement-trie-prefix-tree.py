class TrieNode:
    def __init__(self):
        # children 直接用 dict，key 是字元，value 是下一個 TrieNode
        self.children = {}
        # is_end 標記此節點是否為一個完整單詞的結尾
        self.is_end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            # 若該字元尚未在 children 中，則新建一個子節點
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # 標記單詞結尾
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie (as a complete word), else False.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        # 只有在標記為完整單詞時才算找到
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        # 只要能沿著 prefix 走到最後，就代表存在以此為前綴的單詞
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False (不是完整單詞)
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app"))     # True

