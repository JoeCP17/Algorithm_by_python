# 다른문자가나와야한다.
# 카운터 변수필요
# 있는문자가 또 나올경우 X
# 문자가 겹치지 않는경우 +1
# 메모리 128m 어케줄여 ㅅㅂ 
n = int(input())

def result(aa):
    for i in range(aa):
        word = input()
        for j in range(1, len(word)):
            if word.find(word[j - 1]) > word.find(word[j]):
                aa -= 1

    return aa


print(result(n))
