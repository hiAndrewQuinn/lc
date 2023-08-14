import random


def longestSubstring(s):
    ans, i, seen = 0, 0, set()

    for j in range(len(s)):
        print(f"j: {j}, s[j]: {s[j]}, seen: {seen}".ljust(50), end=" ")
        while s[j] in seen:
            seen.remove(s[i])
            i += 1
        seen.add(s[j])
        print(f"ans = max({ans}, {len(seen)})".ljust(20))
        ans = max(ans, len(seen))

    return ans


if __name__ == "__main__":
    random_string = "".join([chr(random.randint(97, 100)) for _ in range(12)])
    print(random_string)
    print("-" * 70)
    print("Longest substring:", longestSubstring(random_string))
