 # 오라클DB 연동
import cx_Oracle as ora

 # DB 접속함수
def myconn():
    # 데이터소스 네임, 객체 생성(접속주소, 포트번호, 서비스명)
   dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 오라클 주소
   conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='UTF-8') # 오라클 접속
   return conn

def test01(conn):
   cur = conn.cursor() # 실행 결과 데이터를 담을 메모리 객체
   for row in cur.execute('SELECT * FROM emp'):
       print(row)

   cur.close()
   conn.close()

def test02(conn):
   cur = conn.cursor()
   cur.execute('SELECT * FROM emp')
   while True:
       row = cur.fetchone()
       if row is None:
           break
       print(row)
   cur.close()
   conn.close()    

if __name__ == '__main__':
    print('____SQL조회 기본 실행____')
    test01(myconn())
    print('__SQL조회 fetchone 사용 ---')
    test02(myconn())

