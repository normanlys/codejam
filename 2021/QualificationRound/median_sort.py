from typing import List


def question(i: int, j: int, k: int) -> int:
    print(f"{i} {j} {k}")
    return int(input())
    
def solve(N: int, Q: int) -> List[int]:
    result = [0] * N
    sorted_array = list(range(1, N + 1))

    for i in range(1, N - 2):
        median = question(i, i + 1, i + 2)
        

    return result


T, N, Q = list(map(lambda x : int(x), input().split()))

for i in range(T):
    result = solve(N, Q)
    print(" ".join(map(lambda x: str(x), result)))
