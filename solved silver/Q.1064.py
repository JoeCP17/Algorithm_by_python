# 평행사변형은 평행한 두 변을 가진 사각형이다. 세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)
# 이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 이때, D가 여러 개 나올 수도 있다.
# 만들어진 모든 사각형 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오.
# 만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.

from decimal import *

def dist(a, b) :
    return ((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])).sqrt()

getcontext().prec = 28

xa , ya , xb, yb , xc , yc = tuple(map(Decimal , input().split()))
a,b,c = (xa , ya) , (xb , yb) , (xc , yc)
la,lb,lc = dist(b,c) , dist(a,c) , dist(a,b)

if (xb - xa) * (yc -ya) == (yb-ya) * (xc - xa):
    print(-1)

else:
    len_list = [la , lb , lc]
    print((max(len_list) - min(len_list)) * Decimal(2))