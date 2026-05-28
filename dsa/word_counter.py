class Solution:
    def wordCounter(self, sentence: str) -> dict:
        my_dict = {}
        cleaned_sentence = sentence.casefold().split()
        for word in cleaned_sentence:
            my_dict[word] = my_dict.get(word, 0) + 1

        return my_dict


solution = Solution()
sentence = "Apple banana orange apple Banana"
print(solution.wordCounter(sentence))