import math

def get_correct_probability(s: float, q: float) -> float:
    return 1 / (1 + math.exp(q - s))

T = int(input())
P = float(input())

for i in range(T):
    for _ in range(100):
        pass

    print(f"Case #{i+1}: {result}")