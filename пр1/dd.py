n = int(input())

nominals = [10, 5, 2, 1]

ways = [0] * (n + 1)

ways[0] = 1

for i in range(len(nominals)):
    for j in range(nominals[i], n + 1):
        ways[j] += ways[j - nominals[i]]

print(ways[n])