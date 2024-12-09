from selenium import webdriver
import time
import pyperclip
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# 드라이버 초기화 및 설정
driver = None

def init_driver():
    global driver
    driver = uc.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://chat.openai.com/")


def login():
    login_button = driver.find_element(By.XPATH, '//button[@data-testid="login-button"]')
    login_button.click()
    name_box = driver.find_element(By.ID, "username")
    name_box.send_keys("42bergoblin@gmail.com")
    continue_button = driver.find_element(By.CLASS_NAME, "_button-login-id")
    continue_button.click()
    pw_box = driver.find_element(By.ID, "password")
    pw_box.send_keys("godiaksgksek1!")
    continue_button = driver.find_element(By.CLASS_NAME, "_button-login-password")
    continue_button.click()
    time.sleep(5)
    driver.get("https://chat.openai.com/c/08fa9ab9-1bf1-4b8e-8335-dbc801764864")




def main():
    init_driver()

    global driver
    if not driver:
        init_driver()

    # 사용자에게 로그인할 시간 제공
    # print("로그인을 완료한 후, 스크립트를 계속 진행하려면 엔터 키를 누르세요...")
    # input()
    login()

    # 로그인 후 메시지 전송 및 응답 복사
    def send_message(message):
        input_box = driver.find_element(By.ID, "prompt-textarea")
        print(input)
        input_box.send_keys(message)
        send_button = driver.find_element(By.XPATH, '//button[@data-testid="send-button"]')
        send_button.click()

    def copy_latest_response():
        responses = driver.find_elements(By.XPATH, '//div[@data-message-author-role="assistant"]')
        print(responses)
        latest_response = responses[-1].text if responses else "No response found"
        print(latest_response)
        pyperclip.copy(latest_response)

    time.sleep(5)  # 응답 대기
    send_message("오늘 밥 뭐먹을까")
    time.sleep(10)  # 응답 대기
    copy_latest_response()
    print("Copied ChatGPT response:", pyperclip.paste())
    time.sleep(100)  # 응답 대기

    #driver.quit()

if __name__ == "__main__":
    main()
