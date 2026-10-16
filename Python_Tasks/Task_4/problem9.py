# Problem 9: Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    n = list(string)
    for i in range(len(n)):
        if i == position:
            n[i] = character
    a = "".join(n)
    return a

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
