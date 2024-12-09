import sys
import pyautogui
import time
import pyperclip
import os
import random
from selenium import webdriver
import time
import pyperclip
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# 드라이버 초기화 및 설정
driver = None
driver2 =None

def init_driver():
    global driver, driver2
    # Chrome options settings
    chrome_options = uc.ChromeOptions()
    chrome_options2 = uc.ChromeOptions()
    #chrome_options.add_argument("--start-minimized")  # Start Chrome minimized
    # Chrome 웹 드라이버 포트 설정
    chrome_port = 9000

    driver = uc.Chrome(options=chrome_options,port=chrome_port)
    driver.implicitly_wait(5)

    driver.get("https://risuai.xyz/")






def login():
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="login-button"]'))
    )
    login_button.click()
    name_box = driver.find_element(By.ID, "username")
    name_box.send_keys("42bergoblin@gmail.com")
    continue_button = driver.find_element(By.CLASS_NAME, "_button-login-id")
    continue_button.click()
    pw_box = driver.find_element(By.ID, "password")
    pw_box.send_keys("godiaksgksek1!")
    continue_button = driver.find_element(By.CLASS_NAME, "_button-login-password")
    continue_button.click()
   
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://chat.openai.com/")
    )
    driver.get("https://chat.openai.com/g/g-wnGjwVgk7-english-teacher/c/00a84d97-c319-4338-9309-6864c35fb83d")



def send_message_to_risu(message):
    print('보낼 메세지',message)

    
    input_box = WebDriverWait(driver, 5).until(
       EC.presence_of_element_located((By.CLASS_NAME, "input-text"))
    )
    time.sleep(2)
    driver.execute_script("arguments[0].value = arguments[1];", input_box, message)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", input_box)
    send_button = driver.find_element(By.CLASS_NAME, 'lucide-send')
    send_button.click()

def copy_latest_response():
    wait = WebDriverWait(driver, 500)  # Adjust the timeout as needed
    loading_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loadmove')))
    print('로딩')
    completion_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'lucide-send')))
    print('완료 버튼 기다려')
    # 페이지의 모든 'em' 태그를 찾습니다.
    # 'chat' 클래스를 가진 모든 'span' 태그 찾기
    chat_spans = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'chattext')))
    print("스팬스",chat_spans)

    # 마지막 'span' 태그
    last_chat_span = chat_spans[0] if chat_spans else None

    # 마지막 'span' 태그 내의 모든 'p' 태그 추출
    if last_chat_span:
        # 'p' 태그를 찾기 위해 find_elements 메서드 사용
        p_elements = last_chat_span.find_elements(By.TAG_NAME, "p")
        last_chat_texts = [p.text for p in p_elements]
    else:
        last_chat_texts = []

    print(last_chat_texts)
    return last_chat_texts


def send_msg_tokakao2(my_msg, repeat_number):
    # 좌표로 마우스 이동
    pyautogui.moveTo(1666, 928)
    # 마우스 클릭
    pyautogui.click()
    pyperclip.copy(my_msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')

def send_msg_tokakao3(my_msg, repeat_number):
    # 좌표로 마우스 이동
    pyautogui.moveTo(1183, 459)
    # 마우스 클릭
    pyautogui.click()
    pyperclip.copy(my_msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')

def filter_friend(filter_keyword, init_number):
    time.sleep(1)
    # 사람 아이콘 클릭
    try:
        click_img(img_path + 'person_icon.png')
        try:
            click_img(img_path + 'person_icon2.png')
        except Exception as e :
            print('e ', e)
    except Exception as e :
        print('e ', e)
    #X 버튼이 존재한다면 클릭하여 내용 삭제
    # try:
    #     click_img(img_path + 'x.png')
    # except:
    #     pass
    # time.sleep(1)
    # # 돋보기 아이콘 클릭
    click_img(img_path+'search.png')
  
  
    if filter_keyword == '':
        pyautogui.keyDown('esc')
    else:
        pyperclip.copy(filter_keyword)
    time.sleep(1)
    try:
        click_img_plus_x(img_path+'search_icon.png', 15)
    except Exception as e :
        click_img(img_path+'search.png') 

    click_img_plus_x(img_path+'search_icon.png', 15)

    if filter_keyword == '':
        pyautogui.keyDown('esc')
        
    else:
        pyperclip.copy(filter_keyword)
        pyautogui.hotkey('ctrl', 'v')
    for i in range(int(init_number)+1):
        pyautogui.keyDown('down')
    time.sleep(2)


def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y) #맥에서는 2로 나눠줘야함. 윈도에서는 나누면 안됨


def click_img_plus_x(imagePath, pixel):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x + pixel, y) #맥에서는 2로 나눠줘야함. 윈도에서는 나누면 안됨


def doubleClickImg (imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y, clicks=2) #맥에서는 2로 나눠줘야함. 윈도에서는 나누면 안됨


def set_delay():
    delay_time = input("몇 초 후에 프로그램을 실행하시겠습니까? : ")
    print(delay_time + "초 후에 프로그램을 실행합니다.")
    for remaining in range(int(delay_time), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r프로그램 실행!\n")


def logout():
    try:
        click_img(img_path + 'menu.png')
    except Exception as e:
        print('e ', e)
    try:
        click_img(img_path + 'logout.png')
    except Exception as e:
        print('e ', e)


def bye_msg():
    input('프로그램이 종료되었습니다.')


def set_import_msg():
    with open("send_for_text.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        print('======== 아래는 전송할 텍스트입니다. ========\n', text)
        return text


def initialize():
    print('Monitor size : ', end='')
    print(pyautogui.size())
    print(pyautogui.position())
    filter_keyword='목성'
    init_number = 1
    repeat_number=1
    # filter_keyword = input("필터링할 친구 이름. 없으면 enter.  ex) 학생 직장 99 : ")
    # init_number = input("필터링한 친구 기준 시작지점(ex. 필터링된 친구 시작지점) : ")
    # repeat_number = input("반복할 횟수(ex. 필터링 검색된 친구 수) : ")
    print('=================')
    print('메세지 전송 시작!')
    print('=================')
    return (filter_keyword, init_number, repeat_number)


# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.9
pyautogui.PAUSE = 0.5

# 전체복사를 위해 카카오톡 창 찍는 좌표 설정
kakao_x = 1443
kakao_y = 575

# 전체복사를 위해 카카오톡 창 찍는 좌표 설정
kakao_x2 = 965
kakao_y2 = 175

# 이전에 복사한 내용을 저장할 변수
last_copied_line = None
lastmessage = ""

if __name__ == "__main__":
    (filter_keyword, init_number, repeat_number) = initialize()
    init_driver()
    # 사용자가 수동으로 로그인을 완료할 때까지 기다립니다.
    input("로그인을 완료하고 나면, 터미널에서 엔터를 눌러주세요...")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    send_message_to_risu("안녕")
    time.sleep(1) # 답변 대기
    response_message = copy_latest_response()
    for message in response_message:
        send_msg_tokakao2(message, repeat_number)
    lastmessage_lines = response_message[-1].split('\n')
    lastmessage = lastmessage_lines[-1]


    #2번째 사람에게 반복
    # driver.switch_to.window(driver.window_handles[1])
    # send_message_to_risu("안녕")
    # time.sleep(1) # 답변 대기
    # response_message2 = copy_latest_response()
    # for message in response_message2:
    #     send_msg_tokakao3(message, repeat_number)
    # lastmessage_lines2 = response_message2[-1].split('\n')
    # lastmessage2 = lastmessage_lines2[-1]

    while True:
        # 좌표로 마우스 이동
        pyautogui.moveTo(kakao_x, kakao_y)

        # 마우스 클릭
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        # 클립보드에 내용이 복사될 시간을 주기 위해 잠시 대기
        time.sleep(1)

        # 클립보드의 현재 내용 가져오기
        current_content = pyperclip.paste()
        
        # 내용을 줄 단위로 나누기
        lines = current_content.split('\n')
        last_message_index = 0
        # 리스트 순회하며 부분 문자열 포함 여부 확인
        for i, message in reversed(list(enumerate(lines))):
            if lastmessage in message:
                last_message_index = i
                print(f"'{lastmessage}' 부분 문자열이 포함된 마지막 위치: {i}")
                break
        else:
            # 부분 문자열이 리스트에 없는 경우
            print(f"'{lastmessage}' 부분 문자열은 리스트에 없습니다.")

        
        if last_message_index < len(lines)-2 :
            new_content = '\r'.join(lines[last_message_index+1:])
            # 정규 표현식을 사용하여 '내용' 부분만 추출
            cleaned_text = re.sub(r"\[.*?\]\s\[.*?\]\s", "", new_content)
            pattern = re.compile(r"\[?\w+ \d+:\d+\]?\s+\w+\s+(.*)")
       
            matches = pattern.findall(new_content)

            # 모든 '내용' 부분을 하나의 문자열로 연결
            result = ' '.join(matches)
            if not cleaned_text:
                print("추출된 메시지가 없습니다.")
                continue  

            # driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            send_message_to_risu(cleaned_text)
            # time.sleep(5) #답변 대기
            response_message = copy_latest_response()
            for message in response_message:
                send_msg_tokakao2(message, repeat_number)
            #filter_friend(filter_keyword, init_number)
            lastmessage_lines = response_message[-1].split('\n')
            lastmessage = lastmessage_lines[-1]


        # 잠시 대기
        time.sleep(10)

    #     #2번째 사람 확인
    #     pyautogui.moveTo(kakao_x2, kakao_y2)

    #     # 마우스 클릭
    #     pyautogui.click()
    #     pyautogui.hotkey('ctrl', 'a')
    #     pyautogui.hotkey('ctrl', 'c')

    #     # 클립보드에 내용이 복사될 시간을 주기 위해 잠시 대기
    #     time.sleep(1)

    #     # 클립보드의 현재 내용 가져오기
    #     current_content = pyperclip.paste()
        
    #     # 내용을 줄 단위로 나누기
    #     lines = current_content.split('\n')
    #     last_message_index = 0
    #     # 리스트 순회하며 부분 문자열 포함 여부 확인
    #     for i, message in reversed(list(enumerate(lines))):
    #         if lastmessage2 in message:
    #             last_message_index = i
    #             print(f"'{lastmessage2}' 부분 문자열이 포함된 마지막 위치: {i}")
    #             break
    #     else:
    #         # 부분 문자열이 리스트에 없는 경우
    #         print(f"'{lastmessage2}' 부분 문자열은 리스트에 없습니다.")

        
    #     if last_message_index < len(lines)-2 :
    #         new_content = '\r'.join(lines[last_message_index+1:])
    #         # 정규 표현식을 사용하여 '내용' 부분만 추출
    #         cleaned_text = re.sub(r"\[.*?\]\s\[.*?\]\s", "", new_content)
    #         pattern = re.compile(r"\[?\w+ \d+:\d+\]?\s+\w+\s+(.*)")
       
    #         matches = pattern.findall(new_content)

    #         # 모든 '내용' 부분을 하나의 문자열로 연결
    #         result = ' '.join(matches)
    #         if not cleaned_text:
    #             print("추출된 메시지가 없습니다.")
    #             continue  

    #         driver.switch_to.window(driver.window_handles[1])   
    #         time.sleep(1)
    #         send_message_to_risu(cleaned_text)
    #         # time.sleep(5) #답변 대기
    #         response_message2 = copy_latest_response()
    #         for message in response_message2:
    #             send_msg_tokakao3(message, repeat_number)
    #         #filter_friend(filter_keyword, init_number)
    #         lastmessage_line2 = response_message2[-1].split('\n')
    #         lastmessage2 = lastmessage_lines2[-1]
    # bye_msg()


    # else:
    #     long_msg = set_import_msg()
    #     set_delay()
    #     filter_friend(filter_keyword, init_number)
    #     send_msg(long_msg, repeat_number)
    #     logout()
    #     bye_msg()
