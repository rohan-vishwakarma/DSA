def minWindow(s: str, t: str) -> str:
    t = list(t)
    s = list(s)
    result_index = []
    for i in range(0, len(s)):
        if s[i] in t:
            result_index.append(i)
    minimum = min(result_index)
    maximum = max(result_index)

    string = s[minimum:maximum + 1]
    return "".join(map(str, string))


print(minWindow("ADOBECODEBANC", "ABC"))