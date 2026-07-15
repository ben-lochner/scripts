fin = open("INPUT_TESTING.in", "r")
fout = open("OUTPUT_TESTING.out", "w")

ynegative53 = []
# ^ minecraft joke
best = 0
n, k = map(int, fin.readline().split())
for line in (fin):
    ynegative53.append(int(line))
ynegative53.sort()
print(ynegative53)
lowest = min(ynegative53)

for i in range(n):
    lowest = ynegative53[i]
    amount = 0

    for num in ynegative53:
        if num - lowest <= k:
            amount += 1

    if amount > best:
        best = amount

print(str(best) + " diamonds fit in the collection!")

fin.close()
fout.close()
