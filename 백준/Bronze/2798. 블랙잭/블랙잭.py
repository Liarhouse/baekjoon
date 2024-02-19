def find_closest_sum(cards, target):
    closest_sum = 0
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                card_sum = cards[i] + cards[j] + cards[k]
                if card_sum <= target:
                    closest_sum = max(closest_sum, card_sum)
    return closest_sum

# 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 최대한 가까운 카드 3장의 합 찾기
result = find_closest_sum(cards, M)
print(result)
