from typing import List, Pattern


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
            prefixes.append(splitted_patterns[0])
            if len(splitted_patterns[0]) > len(prefixes[i]):
                lp = i
            pattern = pattern[len(splitted_patterns[0]):]
        else:
            prefixes.append("")
            
        if pattern[-1] != "*":
            suffixes.append(splitted_patterns[-1])
            if len(splitted_patterns[0]) > len(suffixes[i]):
                ls = i
            pattern = pattern[:len(pattern)-len(splitted_patterns[-1])]
        else:
            suffixes.append("")

        p.append(pattern)
    print(prefixes)
    print(suffixes)
    for i in range(n):
        if prefixes[i] and prefixes[i] != prefixes[lp][:len(prefixes[i])]:
            print(f"p {i}")
            return "*"
        if suffixes[i] and suffixes[i] != suffixes[ls][len(suffixes[ls])-len(suffixes[i]):len(suffixes[ls])]:
            print(f"s {suffixes[ls][len(suffixes[ls])-len(suffixes[i]):len(suffixes[ls])]}")
            return "*"

    result = prefixes[lp]
    for pattern in p:
        for sp in pattern.split("*"):
            result += sp
    result += suffixes[lp]
    return result


import sys

sys.stdin = open("test.txt", "r")
T = int(input())
for i in range(T):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(input())
    result = solve(arr)
    print(f"Case #{i+1}: {result}")
