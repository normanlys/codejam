import math
from typing import List

def product_of_cards(array: List[int]) -> int:
    if len(array) == 1:
        return array[1]
    else:
        return math.prod(array)

def solve(array: List[int]) -> int:
    total = sum(array)
    max_sum = 0
    # n_product_cards = 1
    # while n_product_cards < len(array):
    #     for i in range(1, n_product_cards+1):
    #         while i > 0:
    #             for j in range(len(array)):
    #                 pass
    #     n_product_cards += 1

    return max_sum

T = int(input())
for i in range(T):
    arr = []
    M = int(input())
    for j in range(M):
        p, n = list(map(int, input().split()))
        arr += [p] * n

    result = solve(arr)
    print(f"Case #{i+1}: {result}")