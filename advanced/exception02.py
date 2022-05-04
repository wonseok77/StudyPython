# 예외처리 2 - 예외발생 2

x , y = map(int, input('두 수를 입력하세요>').split(' '))

print(f'x={x}')
print(f'y={y}')
z = 0

try:
    z = x / y
    print(f'{x} / {y} = {z}')
except TypeError as e:
    print('형변환 하세요')
except ZeroDivisionError as e:
    print('두번째수에 0은 넣지마세요')
except Exception as e:
    print('예외발생 {e}')

print('나누기 종료')

