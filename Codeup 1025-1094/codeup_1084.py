r , g ,b = map(int,input().split())

rgb_occerence = 0

for i in range(0,r):
    for j in range(0,g):
        for k in range(0,b):
            rgb_occerence += 1

            print(i , j , k )


print(rgb_occerence)

