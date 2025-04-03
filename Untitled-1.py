'''
사용자가 정수를 여러 개 입력합니다.
입력된 정수들 중에서 이전 수보다 큰 수의 개수를 출력하는 프로그램을 만드세요.


'''

raw = list(map(int, input(':').split()))
answer = []

for i in raw:
    if i < 0 or i > 100:
        pass
    else:
        answer.append(i)
avg = sum(answer) / len(answer)
print(round(avg, 1))