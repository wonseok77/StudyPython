## 문자열 연산
first = 'Hello'
second = 'World!'

print(first + second) # 문자연산 + (합치기)
print(first, second)

print(first * 3) # 문자열연산 +, *밖에 없음


## 문자열 길이 내장함수
print(len('한글'))
print(len(first))

## 리스트 연산
print(first[4])
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
# print(first[-6]) #IndexError!! 큰문제

## 현재 일시
current_date = '2022-05-02 14:23:45'
year = current_date[0:4]
month = current_date[5:7]
day = current_date[8:10]
hour = current_date[11:13]
min = current_date[14:16]
sec = current_date[17:19]


print('년:',year, '월:',month ,'일', day)
print(hour, '시', min, '분', sec, '초')

print(current_date[-5:-3])

l = [1,2,3,4,5]
l[0] = 10
print(1)

p = 'python'
print(p)
#p[0] = 'p' # Python TypeError
p2 = 'P' + p[1:]

print(p2)

print(p.upper())
print(p2.lower())


