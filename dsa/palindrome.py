class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(s.split()).lower()
        i, j  = 0, len(cleaned_text)-1
        while i < j:
            if cleaned_text[i] != cleaned_text[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


solution = Solution()
s = "Is this True"
print(solution.validPalindrome(s))