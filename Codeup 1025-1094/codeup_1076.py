aa = ord(input())

bb = list()

for i in range(ord('a') , aa+1):
    bb.append(chr(i))

for j in bb:
    print(j , end = " ")
