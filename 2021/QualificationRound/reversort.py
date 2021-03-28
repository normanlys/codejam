from typing import List

def solve(array: List[int]) -> int:
    result = 0
    for i in range(len(array) - 1):
        min_value = min(array[i:])
        j = array.index(min_value)
    
        cost = j - i + 1
        result += cost

        array[i:j+1] = reversed(array[i:j+1])

    return result

T = int(input())
for i in range(T):
    _ = input()
    array = list(map(lambda x : int(x), input().split()))
    result = solve(array)
    print(f"Case #{i+1}: {result}")