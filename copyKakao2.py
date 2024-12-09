# import cv2
# import numpy as np
# import pytesseract
# import pyautogui
# from PIL import Image

# # Tesseract 경로 설정
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # Mac에서 Tesseract 경로

# # 화면에서 이미지 캡처
# x, y, width, height = 1199, 140, 450, 500
# screenshot = pyautogui.screenshot(region=(x, y, width, height))
# screenshot_np = np.array(screenshot)
# gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

# # 이미지 전처리
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# kernel = np.ones((2, 2), np.uint8)
# thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)

# # 텍스트 영역 찾기
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # 인식된 텍스트를 저장할 리스트
# recognized_texts = []

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     # 특정 크기 이상의 텍스트 영역만 처리
#     if w > 10 and h > 10:  # 조절된 크기
#         text_roi = thresh[y:y+h, x:x+w]

#         roi_img = Image.fromarray(text_roi)
#         text = pytesseract.image_to_string(roi_img, lang='kor', config='--psm 6')
#         print(text)
#         if text.strip() != "":
#             recognized_texts.append(text.strip())

# # 각 텍스트 항목에서 줄바꿈 문자를 공백으로 대체
# cleaned_texts = [text.replace('\n', ' ') for text in recognized_texts]
# print(cleaned_texts)

# # 결과 이미지 표시
# cv2.imshow('Detected', screenshot_np)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
import pytesseract
import pyautogui
from PIL import Image

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# 화면에서 이미지 캡처
x, y, width, height = 1199, 40, 400, 600 # 적절한 위치와 크기 조정
screenshot = pyautogui.screenshot(region=(x, y, width, height))
screenshot_np = np.array(screenshot)
gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

# 대비 향상 및 노이즈 제거
enhanced = cv2.detailEnhance(gray, sigma_s=10, sigma_r=0.15)

# 적절한 이진화 적용
_, thresh = cv2.threshold(enhanced, 150, 255, cv2.THRESH_BINARY_INV)

# 텍스트 영역 찾기 및 필터링
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
recognized_texts = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # 특정 크기 이상의 영역만 처리
    if w > 20 and h > 20:
        text_roi = thresh[y:y+h, x:x+w]
        roi_img = Image.fromarray(text_roi)

        # Tesseract를 사용하여 텍스트 추출 (고급 옵션 적용)
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(roi_img, config=custom_config, lang='kor')
        if text.strip():
            recognized_texts.append(text.strip())

# 인식된 텍스트 출력
cleaned_texts = [text.replace('\n', ' ') for text in recognized_texts]
print(cleaned_texts)

# 결과 이미지 표시
cv2.imshow('Detected', screenshot_np)
cv2.waitKey(0)
cv2.destroyAllWindows()
