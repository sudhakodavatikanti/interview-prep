class Solution:
    def reverseWords(self, text: str) -> str:
        words = text.split(" ")
        reverse = ""
        for i in range(len(words)-1, -1 , -1):
            reverse = reverse + " " + words[i]
            print(reverse)

        return reverse


solution = Solution()
text = "I love Playwright" 
print(solution.reverseWords(text))  