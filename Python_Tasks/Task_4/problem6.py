# Problem 6: Find the Runner-Up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_list = sorted(set(arr))
    print(sorted_list[-2])
