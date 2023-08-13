class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True
        

    def search(self, word: str) -> bool:
        def searchTrie(word, node):
            for i in range(len(word)):
                if word[i] == ".":
                    for ch in node:
                        if ch != "$" and searchTrie(word[i + 1:], node[ch]):
                            return True
                    return False
                else:
                    if word[i] not in node:
                        return False
                    node = node[word[i]]
            return "$" in node
        return searchTrie(word, self.trie)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)