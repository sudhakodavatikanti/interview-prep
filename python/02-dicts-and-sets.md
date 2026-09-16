# Dicts & Sets

A dict is a hashtable . When we look up d[key], Python runs key through the built-in hash() function to get an integer, then reduces that interger to an index into an internal array of slots. It jumps directly to the slot - no scanning. That's why look up time barely changes whether the dict has 10 entries or 100. 

It's average time complexiry is O(1) . Worst case is O(n) if many keys hash to the same slot , though Python's implementation make that rare. 

- In dicts we should dict[key] when they key should always be there. You want it to blow up loudly if it's missing, because that's bug. Int his case, it returns KeyError. 

- We use dict.get(key) when a missing key is normal/ expected and you'd rather have a safe fallback than a crash. In this case, it returns None. 



***** Sets ********

- Unordered collection of unique, hashable ietms. No duplicates, no indexing
- Like a dict with keys only, no values. Backed by a hash table

vs list / vs dict

| | list | set | dict |
|---|---|---|---|
| duplicates | yes | no | keys: no |
| ordered | yes | no | yes (insertion, 3.7+) |
| index access | lst[0] | no | by key |
| x in ... | O(n) scan | O(1) avg | O(1) avg (keys) |
| stores | values | values | key → value |

collections.Counter — purpose-built for this:

Alternatives to "if key in dict" 

1. def word_counter(words: list[str]) -> dict[str, int]:
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

2. 
from collections import Counter
counts = Counter(words)          # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
Better: one line, intent is obvious, and you get extras like counts.most_common(2).

collections.defaultdict(int) — auto-creates a missing key with value 0:

3. 
from collections import defaultdict
counts = defaultdict(int)
for word in words:
    counts[word] += 1
Better: no .get dance; counts[word] += 1 just works because the default int() is 0.

Both remove the "handle the missing-key case" boilerplate. In an interview, writing Counter(words) shows you know the standard library; writing the manual .get loop is still a perfectly good fallback answer.



