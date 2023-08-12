import random

def largestRectangleArea(heights) -> int:
    heights.append(0)
    stack = [-1]
    ans = 0

    for i in range(len(heights)):
        print(f"heights[{i}] - stack :: {stack}")
        while heights[i] < heights[stack[-1]]:
            print(f"  !!! heights[{i}] == {heights[i]}  <  {heights[stack[-1]]} == heights[{stack[-1]}]")
            h = heights[stack.pop()]
            print(f"    !!! popped {h} from stack.")
            w = i - stack[-1] - 1
            print(f"    !!! w = {i} - {stack[-1]} - 1 = {w}")
            print(f"    !!! ans = max({ans}, {h * w})")
            ans = max(ans, h * w)
        print(f"- while concluded, pushing {i} onto {stack}...")
        stack.append(i)
    
    return ans

if __name__ == "__main__":
    list_length = 10  # You can change this value as needed

    random_integers = [random.randint(0, 10) for _ in range(list_length)]

    print(random_integers)

    largestRectangleArea(random_integers)
