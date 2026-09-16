"""
Topic 01 - Lists & Tuples - exercises.

Fill in each TODO, then run:  python3 python/exercises/01-lists-and-tuples.py
If it prints "all passed" with no AssertionError, you got them all.

Notes for this topic: python/lists-and-tuples.md
"""


# ---------------------------------------------------------------------------
# Exercise 1 - create and access
# Build a list of the first 5 even numbers starting from 2: [2, 4, 6, 8, 10].
# Then build a tuple of the 3 RGB channel names: ("red", "green", "blue").
# ---------------------------------------------------------------------------
def ex1_create():
    evens = [2,4,6,8,10]
    rgb = ('red', 'green', 'blue')
    return evens, rgb


# ---------------------------------------------------------------------------
# Exercise 2 - mutability
# Given the list, append 4 and change the first element to 99, then return it.
# Then try to do the same to a tuple and CATCH the error - return the name of
# the exception class as a string (e.g. "ValueError").
# ---------------------------------------------------------------------------
def ex2_mutability():
    nums = [1, 2, 3]
    nums.append(4)
    nums[0] = 99
    

    t = (1, 2, 3)
    error_name = None
    try:
        t[0] = 99
    except Exception as e:
        error_name = type(e).__name__

    return nums, error_name


# ---------------------------------------------------------------------------
# Exercise 3 - list methods
# Start from [5, 3, 1, 4, 2].
#   a) return a NEW sorted list, leaving the original untouched  -> use sorted()
#   b) return the original list sorted IN PLACE                  -> use .sort()
#   c) from [1, 2, 3], remove the value 2 and insert 9 at index 0 -> [9, 1, 3]
# ---------------------------------------------------------------------------
def ex3_methods():
    data = [5, 3, 1, 4, 2]
    new_sorted = sorted(data)    
    data.sort()             # (this line is the in-place sort - leave it)
    in_place = data

    lst = [1, 2, 3]
    lst.remove(2)
    lst.insert(0,9)

    return new_sorted, in_place, lst


# ---------------------------------------------------------------------------
# Exercise 4 - slicing
# Given nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] return, using slices only:
#   first_three, last_three, middle (index 3..6 inclusive), reversed_copy,
#   every_other (0, 2, 4, 6, 8)
# ---------------------------------------------------------------------------
def ex4_slicing():
    nums = list(range(10))
    first_three = nums[:3]
    last_three = nums[-3:]
    middle = nums[3:7]
    reversed_copy = nums[::-1]
    every_other = nums[::2]
    return first_three, last_three, middle, reversed_copy, every_other


# ---------------------------------------------------------------------------
# Exercise 5 - tuple unpacking
#   a) swap a and b WITHOUT a temp variable
#   b) return min and max of the list as a single tuple, computed in one line
#   c) given point = (3, 4), unpack into x, y and return x + y
# ---------------------------------------------------------------------------
def ex5_unpacking():
    a, b = 1, 2
    a, b = b, a

    values = [7, 2, 9, 4]
    min_max = (min(values), max(values))

    point = (3, 4)
    x, y = point
    total = x + y

    return (a, b), min_max, total


# ---------------------------------------------------------------------------
# Exercise 6 - hashability
# Use a tuple (row, col) as a dict key to store the value "X" at (1, 2).
# Then show a list can't be a key: attempt board[[1, 2]] = "O", catch it,
# return the exception class name.
# ---------------------------------------------------------------------------
def ex6_hashability():
    board = {}

    board[(1, 2)] = "X"
    error_name = None
    try:
        board[[1, 2]] = "0"
        pass
    except Exception as e:
        error_name = type(e).__name__

    return board, error_name


# ---------------------------------------------------------------------------
# Exercise 7 - shallow immutability
# t = ([1, 2], "fixed"). You cannot reassign t[0], but you CAN mutate the list
# inside it. Append 3 to that inner list and return t.
# Then explain (return the string) why t can't be used as a dict key.
# ---------------------------------------------------------------------------
def ex7_shallow():
    t = ([1, 2], "fixed")
    t[0].append(3)

    reason = "t can't be used as a dict key because it contains a list and it is mutable"  
    return t, reason


# ---------------------------------------------------------------------------
def _run():
    evens, rgb = ex1_create()
    assert evens == [2, 4, 6, 8, 10], evens
    assert rgb == ("red", "green", "blue"), rgb

    nums, err = ex2_mutability()
    assert nums == [99, 2, 3, 4], nums
    assert err == "TypeError", err

    new_sorted, in_place, lst = ex3_methods()
    assert new_sorted == [1, 2, 3, 4, 5], new_sorted
    assert in_place == [1, 2, 3, 4, 5], in_place
    assert lst == [9, 1, 3], lst

    f3, l3, mid, rev, alt = ex4_slicing()
    assert f3 == [0, 1, 2], f3
    assert l3 == [7, 8, 9], l3
    assert mid == [3, 4, 5, 6], mid
    assert rev == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], rev
    assert alt == [0, 2, 4, 6, 8], alt

    ab, min_max, total = ex5_unpacking()
    assert ab == (2, 1), ab
    assert min_max == (2, 9), min_max
    assert total == 7, total

    board, err6 = ex6_hashability()
    assert board == {(1, 2): "X"}, board
    assert err6 == "TypeError", err6

    t, reason = ex7_shallow()
    assert t == ([1, 2, 3], "fixed"), t
    assert len(reason.strip()) > 0, "write a one-sentence reason for ex7"

    print("all passed")


if __name__ == "__main__":
    _run()
