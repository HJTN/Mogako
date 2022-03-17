# 필요한 library 가져오기
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

# 파파고 웹 페이지 접속
# 자동화된 크롬 창 실행
chrome_driver = ChromeDriverManager().install()
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

# 파파고 웹 페이지 접속
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)

# 시간적 여유 3초
time.sleep(3)

# 번역 결과 반환 함수
def return_result(keyword):
    # 영단어 입력, 번역 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").send_keys(keyword)
    driver.find_element(By.CSS_SELECTOR, "button#btnTranslate").click()
    time.sleep(1)

    # 번역 결과 저장
    output = driver.find_element(By.CSS_SELECTOR, "div#txtTarget").text

    # 영단어 입력 칸 초기화
    driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").clear()

    return output

# 한영 전환
def switch():
    driver.find_element(By.CSS_SELECTOR, "button.btn_switch___x4Tcl").click()

    # 영단어 입력 칸 초기화
    driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").clear()

# CSV 파일 'my_papago.csv' 생성
# 작성할 'my_papago.csv' 파일을 생성하여 변수 'f'에 저장
f = open('./my_papago.csv', 'w', newline = '', encoding='euc-kr')

# writer 객체 생성 & 파일의 열 제목 생성
# CSV 파일을 작성하는 객체 변수 'wtr' 생성
wtr = csv.writer(f)
# 열 제목 작성
wtr.writerow(['영단어', '번역결과'])

# Dictionary 생성
my_dict = {}

# 반복문을 활용하여 번역기 구현 및 CSV 파일에 저장
# 무한 루프
while True:
    keyword = input("번역할 영단어 입력 ('0' 입력하면 종료, 'check' 입력하면 현재 사전의 번역 결과 확인) : ")
    if keyword == "0":
        print("번역 종료")
        break
    elif keyword in my_dict.keys():
        print("이미 번역한 영단어입니다! 뜻은", my_dict[keyword], "입니다.")
    elif keyword == 'check':
        switch()

        for result in my_dict.values():
            print(f'{result} : {return_result(result)}')
        
        switch()

    else:
        # my_papago.csv 파일에 [영단어, 번역결과] 작성
        wtr.writerow([keyword, return_result(keyword)])
        my_dict[keyword] = return_result(keyword)

driver.close()
f.close()