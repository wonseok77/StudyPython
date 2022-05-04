# 사람객체를 위한 클래스 Person
from unicodedata import name


class Person:
    __name = '' # 이름속성
    age = 0   # 나이속성
    height = 100 # 키 속성
    weight = 30 # 몸무게

    # 생성자 재정의
    def __init__(self, name = None) -> None:
        if name == None:
            self.__name = '홍길동'
        else:
            self.__name = name
        print(f'{self.__name} 탄생!!')

    # 매직메서드 __str__ 사용 재정의
    def __str__(self) -> str:
        value = f'''객체 : {self.__name}\n
        나이 : {self.age}\n
        키 : {self.age}\n
        '''
        return value

    def walk(self, speed):
        print(f'{self.__name}이(가) {speed}km/h로 걷습니다.')
        return 
    
    def run(self, speed):
        print(f'{self.__name}이(가) {speed}km/h로 달립니다.')


p = Person('장원석') # 객체 생성
#p.__name = '장원석'
p.age = 20
p.height = 177
p.weight = 78
p.walk(2)
p.run(10)

print(p)




