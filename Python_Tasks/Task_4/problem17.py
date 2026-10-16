# Problem 17: Finding the Percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input())
students = {}

for _ in range(n):
    name, *marks = input().split()
    students[name] = list(map(float, marks))

query = input()
print(f"{sum(students[query]) / len(students[query]):.2f}")
