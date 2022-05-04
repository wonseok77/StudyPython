# 예외처리 1 - 예외발생
def multi(a, b):
    res = a * b
    return res

def divide(a, b):
    res = 0

    try:
        res = a / b
    except ZeroDivisionError as e:
        print(f'예외발생 {e}')
    finally:
        return res

if __name__ == '__main__':
    value = 7
    print('곱셈/나눗셈')
    print(divide(6,0))
    print(multi(6,6))
    print('종료')

## 디버깅
# break point F9
# 한스텝씩 넘어가는거 F10
# 하나의 함수로 들어가는거 F11
# 디버그 시작 F5
# 디버깅 나가기 shift F5


