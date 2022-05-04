# # CSV 파일 열기
import csv

file_name = './busanbus_211231.csv'

f= open(file_name, mode = 'r', encoding = 'cp949')
reader = csv.reader(f, delimiter=',') #구분자가 ,일경우

next(reader)
for line in reader:
    print(line)

f.close() ## 필수!!
