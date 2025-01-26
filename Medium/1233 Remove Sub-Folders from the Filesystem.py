# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/


class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        res = []
        folder = sorted(folder)
        root = TrieNode()

        def dfs(folder, subIndex = True):
            curr = root

            folder_val = folder.split("/")

            for i in range(len(folder_val)):
                if folder_val[i] not in curr.children:
                    curr.children[folder_val[i]] = TrieNode()
                curr = curr.children[folder_val[i]]
                if curr.endOfWord:
                    subIndex = False
                    break
            curr.endOfWord = True  

            if subIndex: 
                res.append(folder)

        for i in range(len(folder)):
            dfs(folder[i], True)

        return res
