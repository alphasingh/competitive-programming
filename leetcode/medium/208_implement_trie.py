"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.is_word = False
        self.children = []

    def isWord(self):
        self.is_word = True

    def __str__(self):
        return str(self.value) + '.' + str(self.children) + 'X' + str(self.is_word)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        word_pointer = 0
        word_pointer_limit = len(word)
        trie_pointer = self.root
        while word_pointer < word_pointer_limit:
            for child in trie_pointer.children:
                if child.value == word[word_pointer]:
                    trie_pointer = child
            else:
                trie_pointer.children.append(TrieNode(value=word[word_pointer]))
                trie_pointer = trie_pointer.children[-1]
            word_pointer += 1
        trie_pointer.isWord()
        print(word, trie_pointer)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        word_found = False
        word_pointer = 0
        word_pointer_limit = len(word)
        trie_pointer = self.root
        while word_pointer < word_pointer_limit:
            for child in trie_pointer.children:
                if child.value == word[word_pointer]:
                    trie_pointer = child
                    word_found = True
                    # print(child.value, [str(c) for c in child.children])
            if not word_found:
                break
            word_pointer += 1
        print(trie_pointer)
        return word_found and trie_pointer.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        prefix_found = False
        word_pointer = 0
        word_pointer_limit = len(prefix)
        trie_pointer = self.root
        while word_pointer < word_pointer_limit:
            for child in trie_pointer.children:
                if child.value == prefix[word_pointer]:
                    trie_pointer = child
                    prefix_found = True
            if not prefix_found:
                break
            word_pointer += 1
        return prefix_found


trie = Trie()
trie.insert("word")
assert trie.search("word") is True
assert trie.startsWith("prefix") is False
assert trie.startsWith("w") is True
assert trie.startsWith("wo") is True
assert trie.startsWith("rd") is False

trie.insert("apple")
assert trie.search("apple") is True
assert trie.search("app") is False
assert trie.startsWith("app") is True
trie.insert("app")
assert trie.search("app") is True
