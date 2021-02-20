aa = int(input())

result = 0

for i in range(1,aa+1):
    result += i
    if result >= aa:
        break

print(result)