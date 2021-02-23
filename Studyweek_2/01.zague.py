# 문제
# N 자리 2진수를 오름차순으로 모두 출력해보자.
#
# 입력
# 첫 줄에 정수 N 이 주어진다.
#
# (1 ≤ N ≤ 10)
#
# 출력
# N 자리 2진수를 한 줄에 하나씩
# 오름차순으로 출력한다.

# 1. 10진수 2진수 변환
# 2. 증가될때마다 *2 증가

n = int(input())

a = (2 ** n) -1

for i in range(0,a+1):
    zin = "{0:b}".format(i).zfill(n)
    str(zin)
    a = ' '
    print(a.join(zin))






