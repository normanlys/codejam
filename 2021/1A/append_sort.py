from typing import List, Optional


def solve(array: List[int]) -> int:
    if len(array) == 1:
        return 0

    prev = array[0]
    result = 0

    for n in array[1:]:
        if n > prev:
            prev = n
            continue

        str_n = str(n)
        str_prev = str(prev)

        diff = len(str_prev) - len(str_n)
        if diff == 0:
            result += 1
            new_n = int(str_n + "0")
        elif str_prev.startswith(str_n):
            r = len(str_prev) - 1
            while r >= len(str_n) and str_prev[r] == "9":
                r -= 1

            if r < len(str_n):
                result += diff + 1
                new_n = prev + 1
            else:
                result += diff
                zeros = "0" * (len(str_prev) - r - 1)
                new_n = int(str_prev[:r] + str(int(str_prev[r]) + 1) + zeros)
            
        else:
            result += diff
            new_str_n = str_n + "0" * (diff - 1)
            if new_str_n == str_prev[:len(str_prev)-1] and str_prev[-1] != "9":
                new_str_n += str(int(str_prev[-1]) + 1)
            else:
                new_str_n += "0"
                
            if int(new_str_n) <= prev:
                result += 1
                new_str_n += "0"
            new_n = int(new_str_n)

        # print(n, new_n)
        prev = new_n

    return result
# import sys
# sys.stdin = open("append_sort_test.txt", "r")
T = int(input())
for i in range(T):
    _ = input()
    X = list(map(int, input().split()))
    result = solve(X)
    print(f"Case #{i+1}: {result}")
