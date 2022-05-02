print(id(a))
print(id(b))
print(id(c))



a= 10
b= 20
c= 30

print(a==b)
print(a is b)

a = b
print(a==b)
print(a is b)

# 데이터타입
a = 0b101011
b = 0b11111111
print(a)
print(b)
print(bin(10))

print(0o52)
print(oct(10))

print(0xff)

salery = 4_500_500 # 통화단위
print(salery)

print(type(1))
print(type(3.14))
z = False
print(type(z))

z = 10
print(type(z))

# 여러줄 문자열
multi_line = '''Life is short.
You need Python.
And I need C#, too.
'''

print(multi_line)

# 리스트(배열)
b = [1,2,3,4]
print(b)

b.append(5) # 뒤에 추가
print(b)

b.insert(3,10) #원하는 인덱스에 추가
print(b)

b.sort() #오름차순 정렬
print(b)

b.reverse() # 내림차순 정렬
print(b)

b.remove(10) #원소 삭제
print(b)

print(type(b))
print(b[2])

## 튜플
c = (1,2,3,4)
print(c)

# c.append(5) # error 튜플에서는 값 추가불가
print(c[2])

## 딕셔너리 key : value의 집합
spiderman = { 'name' : 'Peter Parker', 'age' : 18, 'weapon' : 'web shooter' ,'memberOfavengers' : True}
print(spiderman)
print(spiderman['name'])

