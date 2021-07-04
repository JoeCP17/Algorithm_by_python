# 요세푸스 문제는 다음과 같다.
#
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
#
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())  # N , K 값 입력받음

array_1 = [i for i in range(1, N + 1)]  # 범위를 도는 반복문

answer = []  # 빠진 인원들 넣는 배열
num = 0  # 남은 인원 카운트

for j in range(N):
    num += K - 1  # 한명씩 뺀 값을 num 삽입
    if num >= len(array_1):  # num >= array_1의 길이 라면
        num = num % len(array_1)  # 나머지 인원들 num 삽입

    answer.append(str(array_1.pop(num)))  # answer에 삽입

print("<", ",".join(answer)[:], ">", sep='')  # 해당 삽입 인원들 출력
