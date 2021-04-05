from typing import List


def solve(arr: List[str]) -> str:
    n = len(arr)
    lp = 0
    ls = 0
    prefixes = [] 
    suffixes = []
    p = []

    for i in range(n):
        pattern: str = arr[i]
        splitted_patterns = pattern.split("*")

        if pattern[0] != "*":
            current_prefix = splitted_patterns[0]
            prefixes.append(current_prefix)
            if len(current_prefix) > len(prefixes[lp]):
                lp = i
            pattern = pattern[len(current_prefix):]
        else:
            prefixes.append("")
            
        if pattern[-1] != "*":
            current_suffix = splitted_patterns[-1]
            suffixes.append(current_suffix)
            if len(current_suffix) > len(suffixes[ls]):
                ls = i
            pattern = pattern[:len(pattern)-len(current_suffix)]
        else:
            suffixes.append("")

        p.append(pattern)

    for i in range(n):
        if prefixes[i] and prefixes[i] != prefixes[lp][:len(prefixes[i])]:
            return "*"
        if suffixes[i] and suffixes[i] != suffixes[ls][len(suffixes[ls])-len(suffixes[i]):len(suffixes[ls])]:
            return "*"

    result = prefixes[lp]
    for pattern in p:
        for sp in pattern.split("*"):
            result += sp
    result += suffixes[ls]
    return result


T = int(input())
for i in range(T):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(input())
    result = solve(arr)
    print(f"Case #{i+1}: {result}")
