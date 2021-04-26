from typing import List


def solve(a: int, b: int, c: int) -> List[int]:
    is_divisible_by_12 = False
    is_divisible_by_720 = False

    while not is_divisible_by_12 or not is_divisible_by_720:
        a -= 1
        b -= 1
        c -= 1

        is_divisible_by_12 = a % 12 == 0 or b % 12 == 0 or c % 12 == 0


T = int(input())
for i in range(T):
    A, B, C = list(map(int, input().split(" ")))
    result = solve(A, B, C)
    print(f"Case #{i+1}: {' '.join(result)}")

"""
1 12 720 for h m s nanosec

h hand can only point to a num if both s and m hands are overlapping and pointing at a num
tick must be divisible by 720 if rotated 30 degrees


m hand can only point to a num if s hand is pointing at a num, 
tick must be divisible by 12 if rotated 30 degrees

1. rotate them to correct position
2. get time

"""