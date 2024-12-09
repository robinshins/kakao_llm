import pyautogui
import time

def get_mouse_position():
    try:
        print("5초 후에 마우스 좌표를 출력합니다...")
        # 5초 대기
        time.sleep(5)
        
        # 현재 마우스 커서의 x, y 좌표 가져오기
        x, y = pyautogui.position()
        position_str = f'X: {x}, Y: {y}'
        
        # 좌표 출력
        print(position_str)
            
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    get_mouse_position()
