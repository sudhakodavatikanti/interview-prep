"""
Merge overlapping test windows

A test environment has multiple reservation windows:

windows = [[1, 4], [2, 6], [8, 10], [9, 12]]

Merge every overlapping window and return:

[[1, 6], [8, 12]]

Complete:

def merge_test_windows(windows: list[list[int]]) -> list[list[int]]:
    pass
    
"""

class Solution:
    def merge_overlapping_windows(self, windows: list[list[int]]) -> list[list[int]]:
        result = []
        if not windows:
            return []

        sorted_windows = sorted(windows)
        result = [sorted_windows[0].copy()]
        

        for current_window in sorted_windows[1:]:
            last_merged = result[-1]

            if last_merged[1] >= current_window[0]:
                last_merged[1] = max(last_merged[1], current_window[1])

            else:
                result.append(current_window.copy())


        return result



solution = Solution()
windows = [[1,4], [8,10], [2,6], [9,12]]
print(solution.merge_overlapping_windows(windows))