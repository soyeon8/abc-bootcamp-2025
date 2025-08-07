# 팩토리얼 계산 함수
def factorial(n):
    if n < 0:
        raise ValueError("음수에 대한 팩토리얼은 정의되지 않습니다.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
