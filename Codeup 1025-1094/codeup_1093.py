a = int(input())
b = input().split()

arr = [0] * 24

for i in range(a):
    arr[int(b[i])] += 1

for i in range(1,len(arr)) :
    print(arr[i] , end = ' ')