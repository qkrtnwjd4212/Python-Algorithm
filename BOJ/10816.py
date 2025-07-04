# 백준 10816 - 숫자 카드 2
import sys
from collections import Counter
def input(): return sys.stdin.readline()

N = int(input()) # 숫자 카드의 개수
card = list(map(int, input().split()))

M = int(input()) # 정수
num = list(map(int, input().split()))
card_count = Counter(card)

result = []
for n in num:
    result.append(card_count[n])

print(' '.join(map(str, result)))
