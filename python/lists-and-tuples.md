# Lists vs Tuples

Refresher — one line per idea.

- Core difference is **mutability**: list = mutable, tuple = immutable (fixed once created).
- `list` has many methods (`append`, `pop`, `sort`, ...); `tuple` has only `count` and `index`.
- `tuple` uses less memory (sized exactly); `list` over-allocates for growth.
- `t[0] = 99` on a tuple **raises `TypeError`** — it does not silently ignore the write.
- Tuple immutability is **shallow**: in `([1,2], 3)` the inner list can still be mutated.
- A `list` is **never hashable** (mutable by design) → can't be a dict key or set member.
- A `tuple` is hashable **only if all its elements are** → `(1,2)` works as a key, `([1],2)` does not.
- Use a **list** for a variable-length, ordered, homogeneous collection (cart, todo, results).
- Use a **tuple** for a fixed record where position has meaning (`(lat, lng)`, `(host, port)`, DB row), or when you need a dict key, or to signal "don't mutate this."

### Self-check

1. Error from `t[0] = 99`? → `TypeError`, tuples don't support item assignment.
2. Can `([1, 2], 3)` be a dict key? → No, it contains a list (unhashable).
3. Is tuple immutability deep? → No, shallow — inner mutables can change.
