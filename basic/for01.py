# for문 학습
arr = [1,2,3,4,5,6,7,8,9,10]


result = 0
for x in range(1 , 101):
    result = result + x
print('배열의 합 = ', result)


arr2 = ('me','my','friend','jane')
for x in arr2:
    print(f'{x:>10}')

for item in arr2:
    print(f'{item * 2}')

## 1~10까지 수에서 짝수 구분하기

for num in range(1,11):
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 홀수입니다.')


# for문 내에서 사용하는 continue, break
