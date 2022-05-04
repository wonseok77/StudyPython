# 파일 입출력 1 - 쓰기

# mode = w 새로생성쓰기 a 추가쓰기 r 읽기
f = open(file = 'c:/STUDY/StudyPython/temp.txt', mode='a', encoding = 'utf-8')

f.write('\n안녕하세요.\n')
f.write('저는 장원석입니다.\n')
f.write('한국사람이죠.')

f.close() ## 필수
print('파일 생성완료')

