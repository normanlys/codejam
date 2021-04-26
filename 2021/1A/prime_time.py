from collections import OrderedDict


def solve(ordered_dict: OrderedDict) -> int:
    sum_all = 0
    for p, n in ordered_dict.items():
        sum_all += p * n

    for sum_of_product_cards in range(2, 7000):
        product: int = sum_all - sum_of_product_cards
        if product <= 1:
            break

        ok = True
        we_got_sum: int = 0
        for p, n in ordered_dict.items():
            count = 0
            while product % p == 0:
                product //= p
                count += 1

            if count > n:
                ok = False
                break

            we_got_sum += count * p

        if not ok:
            continue

        if product == 1 and we_got_sum == sum_of_product_cards:
            return sum_all - sum_of_product_cards

    return 0


# import sys

# sys.stdin = open("prime_time_test.txt", "r")

T = int(input())
for i in range(T):
    d = OrderedDict()
    M = int(input())
    for j in range(M):
        p, n = list(map(int, input().split()))
        d[p] = n

    result = solve(d)
    print(f"Case #{i+1}: {result}")
