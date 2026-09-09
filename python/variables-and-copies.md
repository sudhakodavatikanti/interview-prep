# Variables, References & Copies

Refresher — one line per idea.

- A variable is a **name bound to an object**, not a box holding a value.
- `b = a` copies the **reference**, not the object → both names point at one object.
- Mutating through either name shows through the other: `a=[1,2,3]; b=a; b.append(4)` → `a == [1,2,3,4]`.
- Real copy: `a.copy()` / `list(a)` / `a[:]` — but this is **shallow** (nested mutables still shared).
- Full independent copy of nested structure: `copy.deepcopy(a)`.
- Applies to every mutable type: list, dict, set, class instances.
- `is` checks **same object** (identity); `==` checks **same value** (equality).

### Self-check

1. Does `b = a` copy the list? → No, same object, two names.
2. `a = [[1,2]]; b = a[:]; b[0].append(9)` — what is `a`? → `[[1, 2, 9]]` (shallow copy shares the inner list).
3. Difference between `is` and `==`? → identity vs value.
