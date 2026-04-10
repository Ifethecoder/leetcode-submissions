from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        To group the anagrams, we can use the sorted str as keys
        and the strs will be mapped to a key
        In the end we return the values
        """

        wordDict = defaultdict(list)

        for word in strs:
            newWord = tuple(sorted(word))
            wordDict[newWord].append(word)
        
        return list(wordDict.values())