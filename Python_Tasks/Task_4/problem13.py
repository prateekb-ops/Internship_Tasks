# Problem 13: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
M = int(input())
a = set(map(int, input().split()))

N = int(input())
b = set(map(int, input().split()))

print(*sorted(a ^ b), sep="\n")
