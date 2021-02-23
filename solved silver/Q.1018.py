# 브루트포스 문제

n , m = map(int,input().split())   # n 그리고 m의 입력값을 받는다.

board = [] # 받은 입력값으로 보드판을 만들기 위한 리스트 선언
mini = [] # 다시 칠해야하는 최소개수를 구하기위한 리스트 선언

for k in range(n): 
    board.append(input())

for a in range(n-7):
    for i in range(m-7):
        idx1 = 0
        idx2 = 0

        for b in range(a , a+8):
            for j in range(i , i+8):

                if (j+b) % 2 ==0:
                    if board[b][j] != 'W' :
                        idx1 += 1
                    if board[b][j] != 'B':
                        idx2 += 1
                else:
                    if board[b][j] != 'B':
                        idx1 += 1
                    if board[b][j] != 'W':
                        idx2 += 1
        mini.append(idx1)
        mini.append(idx2)


print(min(mini))