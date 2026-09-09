# Function Arguments

Refresher — one line per idea.

## How arguments are passed

- Python is **"pass by object reference"** (call by sharing) — neither pass-by-value nor pass-by-reference.
- The parameter is a new name bound to the **same object** the caller passed.
- **Mutating** the object inside the function (`.append`, `x[i]=`, `.update`) → caller sees it.
- **Rebinding** the parameter (`x = [1,2,3]`) → only the local name moves; caller is unaffected.
- Immutable args (int, str, tuple) can't be mutated, so they always look "copied" — same mechanism.

## Mutable default argument trap

- `def f(x, acc=[]): acc.append(x); return acc` — the `[]` is created **once, at def time**.
- Repeated calls reuse the same list: `f(1)` → `[1]`, `f(2)` → `[1, 2]`.
- Fix: default to `None`, build the fresh object in the body:
  ```python
  def f(x, acc=None):
      if acc is None:
          acc = []
      acc.append(x)
      return acc
  ```

### Self-check

1. Pass-by-value or pass-by-reference? → Neither — pass by object reference.
2. Function does `x = [1,2,3]` on its param — does the caller see it? → No, that's a rebind.
3. `def f(x, acc=[])` called twice with 1 then 2? → `[1]`, then `[1, 2]`.
