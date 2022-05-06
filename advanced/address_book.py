# 주소록 프로그램 v1.1
# 작성일 : 2022-05-04
# 작성자 : Wonseok Jang
# 설  명 : 와, 내일 논다~!!
import os
# 연락처 클래스
class Contact:
    name = ''; phone_num = ''; e_mail = ''; addr = ''

    def __init__(self, name, phone_num, e_mail, addr) -> None:
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr
        pass

    def __str__(self) -> str:
        str_val =  (f'이  름 : {self.name}\n'
                    f'핸드폰 : {self.phone_num}\n'
                    f'이메일 : {self.e_mail}\n'
                    f'주  소 : {self.addr}\n'
                    f'==============================')
        return str_val

def run():
    lst_contact = [] # 빈 리스트 생성
    load_contact(lst_contact) # 파일DB 읽어오기
    clearConsole()
    while True:
        sel_menu = get_menu()
        if  sel_menu == 1:
            clearConsole()
            contact = set_contact()
            if contact is None:  
                input('계속하려면 엔터를 누르세요')
                clearConsole()
                continue # contact가 비면 리스트 추가 불가
            lst_contact.append(contact)
            input('연락처 추가성공\n계속하려면 엔터를 누르세요') # 아무값도 안받고 엔터 대기
            clearConsole()
        elif sel_menu == 4: # 종료
            save_contact(lst_contact) # 파일 DB 저장
            break
        elif sel_menu == 2:
            clearConsole()
            get_contact(lst_contact)
            input('계속하려면 엔터를 누루세요')
            clearConsole()
        elif sel_menu == 3:
            clearConsole()
            name = input('삭제할 이름 입력 >')
            del_contact(lst_contact, name)
            input('연락처 삭제성공\n계속하려면 엔터를 누르세요')
            clearConsole()
        else:
            clearConsole()

# 주소록 입력함수
def set_contact():
    contact = None
    try: # 아무입력없이 엔터 갯수 틀리면 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /))').split('/')
        contact = Contact(name, phone_num, e_mail, addr)
    except Exception as e:
        print('입력갯수 확인(이름/핸드폰/이메일/주소)')
    finally:
        return contact # 잘못되면 None리턴, Contact객체 리턴

# 주소록 전체 출력
def get_contact(lst_contact):
    for contact in lst_contact:
        print(contact)

# 삭제 메서드
def del_contact(lst_contact, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]

# 주소록 파일DB 저장
def save_contact(lst_contact):
    f = open('./advanced/db_contact.txt', mode = 'w', encoding = 'utf-8')
    for contact in lst_contact:
        f.write(contact.name + '/')
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')
    
    f.close()

# 주소록 파일DB 로드
def load_contact(lst_contact):
    f = open('./advanced/db_contact.txt', mode = 'r', encoding = 'utf-8')
    while True:
        line = f.readline()
        if not line: break

        lines = line.rstrip('\n').split('/') # \n 제거하고, /로 나누고 리스트로 
        if len(lines) != 4: continue ##220506 11:!1 엔터로 생기는 예외처리
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        lst_contact.append(contact)

    f.close()


# 메뉴 출력 및 선택
def get_menu():
    str_menu = ('---주소록 프로그램 v1.1--\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    # 0-9숫자 외에는 ValueError 발생
    menu = 0 # 초기화
    
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e:
        print(e)
    finally:
        return menu

    
    return int(menu)

def clearConsole():
    command = 'clear' # mac, unix, linux 명령어
    if os.name in ('nt','dos'):
        command = 'cls' #windows, dos 화면클리어 명령
    os.system(command)


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt as e:
        print('Ctril+c 종료')

    print('--주소록 프로그램 v1.1--')
