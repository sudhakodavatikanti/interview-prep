class Solution:
    def topKFrequentWords(self, words: list, k: int) -> list:
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        print(word_count)
        sorted_words = sorted(word_count.items(), key = lambda item:item[1], reverse=True)
        print(sorted_words)

        result = []
        for i in range(k):
            result.append(sorted_words[i][0])

        print(result)
        return result
        
    

solution = Solution()
words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "kiwi"
]

k = 2


        