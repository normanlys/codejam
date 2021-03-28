from typing import List, Optional


def solve(N: int, C: int) -> Optional[List[int]]:
    if C < N - 1 or C > sum(range(2, N + 1)):
        return None
    
    c = C
    n = N
    # sorted_array = list(range(1, N + 1))
    result = [0] * N
    current_num = 1
    while c > n + n - 2:
        if current_num % 2 == 1:
            index = len(result) - int(current_num/2) - 1
        else:
            index = int(current_num/2) - 1
        result[index] = current_num

        c -= n
        n -= 1
        current_num += 1

    length_to_reverse = c - (n - 2)
    sub_result = list(range(current_num, N + 1))
    sub_result[:length_to_reverse] = reversed(sub_result[:length_to_reverse])
    if current_num % 2 == 0:
        sub_result.reverse()

    beginning_index = int((current_num-1)/2)
    result[beginning_index:beginning_index + len(sub_result)] = sub_result
    
    return result

T = int(input())
for i in range(T):
    N, C = list(map(lambda x : int(x), input().split()))
    result = solve(N, C)
    statement = " ".join(list(map(str, result))) if result is not None else "IMPOSSIBLE"
    print(f"Case #{i+1}: {statement}")

