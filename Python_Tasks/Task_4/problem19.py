# Problem 19: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

X = int(input())
sizes = Counter(map(int, input().split()))
N = int(input())

total = 0

for _ in range(N):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        total += price
        sizes[size] -= 1

print(total)
