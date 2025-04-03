# 정수 4 개를입력받아 평균을 반환하는 함수를 작성하시


def sum (input1, input2, input3, input4):
    answer = input1 + input2 + input3 + input4
    return answer


def avg(input1, input2, input3, input4):
    return sum(input1, input2, input3, input4) / 4


print(sum(2, 2, 1, 3))
print(avg(2, 2, 1, 3)) 