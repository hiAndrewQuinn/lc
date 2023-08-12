# `lc` - some annotated LeetCode problems

I started doing LeetCode for fun over my 2023 summer holiday, and I eventually ran into
a few problems where the algorithm just didn't make sense to me until I painstakingly
wrote out some print statements to make it all clear. This git repo is meant to be an
occasional dumping point for such algorithms.

You should be able to run any algorithm here with **no external dependences** by just
running, e.g.

```bash
python 0084_largest-rectangle-in-histogram.py
```

```
Starting random integers:[5, 4, 3, 3, 5, 7, 7, 1, 6, 8]
================================================================================
heights[0] - stack :: [-1]
- while concluded, pushing 0 onto [-1]...
heights[1] - stack :: [-1, 0]
  !!! heights[1] == 4  <  5 == heights[0]
    !!! popped 5 from stack.
    !!! w = 1 - -1 - 1 = 1
    !!! ans = max(0, 5)
- while concluded, pushing 1 onto [-1]...
heights[2] - stack :: [-1, 1]
  !!! heights[2] == 3  <  4 == heights[1]
    !!! popped 4 from stack.
    !!! w = 2 - -1 - 1 = 2
    !!! ans = max(5, 8)
- while concluded, pushing 2 onto [-1]...

[...]

heights[10] - stack :: [-1, 7, 8, 9]
  !!! heights[10] == 0  <  8 == heights[9]
    !!! popped 8 from stack.
    !!! w = 10 - 8 - 1 = 1
    !!! ans = max(21, 8)
  !!! heights[10] == 0  <  6 == heights[8]
    !!! popped 6 from stack.
    !!! w = 10 - 7 - 1 = 2
    !!! ans = max(21, 12)
  !!! heights[10] == 0  <  1 == heights[7]
    !!! popped 1 from stack.
    !!! w = 10 - -1 - 1 = 10
    !!! ans = max(21, 10)
- while concluded, pushing 10 onto [-1]...
================================================================================
Final answer: 21
```
