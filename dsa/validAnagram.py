class Solution:
    def validAnagram(self, s:str, t: str) -> bool:
       if len(s) != len(t):
        return False

       my_dict_1 = {}
       my_dict_2 = {}

       for char in s:
        my_dict_1[char] = my_dict_1.get(char, 0) +1

       for char in t:
        my_dict_2[char] = my_dict_2.get(car, 0) + 1

        for item in my_dict_1:
            if item not in my_dict_2 or my_dict_1[item] != my_dict_2[item]:
                return False

        return my_dict_1 == my_dict_2

solution = Solution()
s = "Listen" , t = "Silent"
print