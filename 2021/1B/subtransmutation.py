import numpy as np

N, A, B = [0, 0, 0]
U = []


def solve() -> str:
    dp = []

    for i in range(1, 100):
        current_best = list(np.zeros(N, dtype=int))

        a = i - A
        if 1 <= a:
            if a <= N and U[a - 1] > current_best[a - 1]:
                current_best[a - 1] = 1
            else:
                prev_best = dp[a - 1]
                for j in range(N):
                    current_best[j] += prev_best[j]

        b = i - B
        if 1 <= b:
            if b <= N and U[b - 1] > current_best[b - 1]:
                current_best[b - 1] += 1
            else:
                prev_best = dp[b - 1]
                for j in range(N):
                    current_best[j] += prev_best[j]

        ok = True
        for j in range(N):
            if current_best[j] < U[j]:
                ok = False
                break

        if ok:
            return i

        dp.append(current_best.copy())

    return "IMPOSSIBLE"


T = int(input())
for i in range(T):
    N, A, B = list(map(int, input().split(" ")))
    U = list(map(int, input().split(" ")))
    result = solve()
    print(f"Case #{i+1}: {result}")
