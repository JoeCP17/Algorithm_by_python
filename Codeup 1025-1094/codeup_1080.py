aa = int(input())
sum = 0
final = 0
for i in range(1, aa+1):
    sum += i
    if sum >= aa:
        final = i
        break


print(final)