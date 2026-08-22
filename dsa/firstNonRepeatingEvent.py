"""
Given a list of event names, return the index of the first event that occurs exactly once. Return -1 if every event is repeated.

def first_unique_event(events: list[str]) -> int:
    pass

Examples:

["login", "search", "login", "checkout"]
# Output: 1
# "search" is the first event occurring once.


["start", "stop", "start", "stop"]
# Output: -1


["error"]
# Output: 0

"""

class Solution:
    def first_unique_events(self, events: list[str]) -> int:
        event_dict = {}

        for event in events:
            event_dict[event] = event_dict.get(event, 0) + 1

        for index, event in enumerate(events):
            if event_dict[event] == 1:
                return index

        return -1


solution = Solution()
events = ["meters", "centi", "meters", "feet", "yards"]
print(solution.first_unique_events(events))