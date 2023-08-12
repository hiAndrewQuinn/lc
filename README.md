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
[10, 9, 2, 2, 3, 2, 0, 0, 1, 8]
heights [0] - stack :: [-1]
- while concluded, pushing 0 onto [-1]...
heights [1] - stack :: [-1, 0]
  !!! heights [1] == 9  <  10 == heights [0]
    !!! popped 10 from stack.
    !!! w = 1 - -1 - 1 = 1
    !!! ans = max(0, 10)
- while concluded, pushing 1 onto [-1]...
heights [2] - stack :: [-1, 1]
  !!! heights [2] == 2  <  9 == heights [1]
    !!! popped 9 from stack.
    !!! w = 2 - -1 - 1 = 2
    !!! ans = max(10, 18)
- while concluded, pushing 2 onto [-1]...

[...]

heights [10] - stack :: [-1, 6, 7, 8, 9]
  !!! heights [10] == 0  <  8 == heights [9]
    !!! popped 8 from stack.
    !!! w = 10 - 8 - 1 = 1
    !!! ans = max(18, 8)
  !!! heights [10] == 0  <  1 == heights [8]
    !!! popped 1 from stack.
    !!! w = 10 - 7 - 1 = 2
    !!! ans = max(18, 2)
- while concluded, pushing 10 onto [-1, 6, 7]...
Starting random integers:[1, 7, 8, 8, 3, 8, 5, 5, 2, 0]
================================================================================
heights [0] - stack :: [-1]
- while concluded, pushing 0 onto [-1]...
heights [1] - stack :: [-1, 0]
- while concluded, pushing 1 onto [-1, 0]...
heights [2] - stack :: [-1, 0, 1]
- while concluded, pushing 2 onto [-1, 0, 1]...
heights [3] - stack :: [-1, 0, 1, 2]
- while concluded, pushing 3 onto [-1, 0, 1, 2]...
heights [4] - stack :: [-1, 0, 1, 2, 3]
  !!! heights [4] == 3  <  8 == heights [3]
    !!! popped 8 from stack.
    !!! w = 4 - 2 - 1 = 1
    !!! ans = max(0, 8)
  !!! heights [4] == 3  <  8 == heights [2]
    !!! popped 8 from stack.
    !!! w = 4 - 1 - 1 = 2
    !!! ans = max(8, 16)
  !!! heights [4] == 3  <  7 == heights [1]
    !!! popped 7 from stack.
    !!! w = 4 - 0 - 1 = 3
    !!! ans = max(16, 21)
- while concluded, pushing 4 onto [-1, 0]...
heights [5] - stack :: [-1, 0, 4]
- while concluded, pushing 5 onto [-1, 0, 4]...
heights [6] - stack :: [-1, 0, 4, 5]
  !!! heights [6] == 5  <  8 == heights [5]
    !!! popped 8 from stack.
    !!! w = 6 - 4 - 1 = 1
    !!! ans = max(21, 8)
- while concluded, pushing 6 onto [-1, 0, 4]...
heights [7] - stack :: [-1, 0, 4, 6]
- while concluded, pushing 7 onto [-1, 0, 4, 6]...
heights [8] - stack :: [-1, 0, 4, 6, 7]
  !!! heights [8] == 2  <  5 == heights [7]
    !!! popped 5 from stack.
    !!! w = 8 - 6 - 1 = 1
    !!! ans = max(21, 5)
  !!! heights [8] == 2  <  5 == heights [6]
    !!! popped 5 from stack.
    !!! w = 8 - 4 - 1 = 3
    !!! ans = max(21, 15)
  !!! heights [8] == 2  <  3 == heights [4]
    !!! popped 3 from stack.
    !!! w = 8 - 0 - 1 = 7
    !!! ans = max(21, 21)
- while concluded, pushing 8 onto [-1, 0]...
heights [9] - stack :: [-1, 0, 8]
  !!! heights [9] == 0  <  2 == heights [8]
    !!! popped 2 from stack.
    !!! w = 9 - 0 - 1 = 8
    !!! ans = max(21, 16)
  !!! heights [9] == 0  <  1 == heights [0]
    !!! popped 1 from stack.
    !!! w = 9 - -1 - 1 = 9
    !!! ans = max(21, 9)
- while concluded, pushing 9 onto [-1]...
heights [10] - stack :: [-1, 9]
- while concluded, pushing 10 onto [-1, 9]...
================================================================================
Final answer: 21
