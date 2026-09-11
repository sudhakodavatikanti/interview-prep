
from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        word_dict = defaultdict(list)
        for word in words:
            sorted_word = ''.join(sorted(word))
            word_dict[sorted_word].append(word)

        return list(word_dict.values())

       

solution = Solution()
words = []
print(solution.groupAnagrams(words))


