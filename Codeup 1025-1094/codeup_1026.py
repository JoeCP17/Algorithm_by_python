# 입력되는 시:분:초 에서 분만 출력해보자.
#
# 참고
# int h, m, s;
# scanf("%d:%d:%d", &h, &m, &s);
#
# 를 실행하면 콜론을 사이에 둔 형식으로 입력되어, h, m, s에 각각 정수값만 저장된다.


h , m , s  = map(int,input().split(':'))

print(m)