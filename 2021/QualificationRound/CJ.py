def solve(x: int, y: int, s: str) -> int:
    if len(s) == 1:
        return 0

    result = 0
    l = 0
    h = 1
    while h < len(s):
        if "?" == s[h]:
            h += 1
            continue
        
        if s[l] == "?":
            pass
        elif s[h] != s[l]:
            result += x if s[l] == "C" else y
        l = h
        h += 1
        
    return result

T = int(input())
for i in range(T):
    inputs = input().split()
    result = solve(int(inputs[0]), int(inputs[1]), inputs[2])
    print(f"Case #{i+1}: {result}")
