import sys
from typing import List


def get_median(i: int, j: int, k: int) -> int:
    print(f"{i} {j} {k}", flush=True)
    return int(input())
    
def solve(N: int) -> List[int]:
    result = []

    first_median = get_median(1, 2, 3)
    if first_median == 1:
        result = [2,1,3]
    elif first_median == 2:
        result = [1,2,3]
    else:
        result = [1,3,2]

    current_unknown = 4
    while current_unknown <= N:
        right = 1
        while True:
            median = get_median(current_unknown, result[right-1], result[right])
            if median == result[right-1]:
                result.insert(right-1, current_unknown)
                break
            elif median == current_unknown:
                result.insert(right, current_unknown)
                break
            else:
                if right == len(result) - 1:
                    result.append(current_unknown)
                    break
                else:
                    right += 1

        current_unknown += 1

    return result


T, N, Q = list(map(int, input().split()))

for i in range(T):
    result = solve(N)
    print(" ".join(map(str, result)), flush=True)

    is_correct = int(input())
    if is_correct != 1:
        sys.exit(1)
