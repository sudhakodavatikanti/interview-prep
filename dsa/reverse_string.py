from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0; j = len(s)-1
        print(i)
        print(j)
        while i < j:
            tmp = s[j]
            s[j] = s[i]
            s[i] = tmp

            print(s)
            i += 1
            j -= 1


solution = Solution()
s = ["s", 'u', 'd', 'h', 'a']
print(solution.reverseString(s))         