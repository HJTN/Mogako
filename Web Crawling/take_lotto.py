# Library 가져오기
from tracemalloc import start
from cv2 import sort
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = ChromeDriverManager().install()
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

# 동행 복권 사이트 접속
login_url = "https://www.dhlottery.co.kr/gameResult.do?method=statByNumber"
driver.get(login_url)
time.sleep(2)

start_num = input('시작 회차를 입력하세요(1회차부터 시작)')
end_num = input('마지막 회차를 입력하세요(최근 회차: 1003회)')
is_add = input('보너스 번호를 추가할까요?(0: 예, 1: 아니오)')

# 보너스 번호 포함 여부 체크
xpath = f'/html/body/div[3]/section/div/div[2]/div/form/table/tbody/tr[1]/td/select/option[{int(is_add)+1}]'
driver.find_element(By.XPATH, xpath).click()
time.sleep(1)

# 회차 선택
# 시작 회차 선택
xpath = f'/html/body/div[3]/section/div/div[2]/div/form/table/tbody/tr[2]/td/select[1]/option[{1003-int(start_num)+1}]'
driver.find_element(By.XPATH, xpath).click()
time.sleep(1)
# 끝 회차 선택
xpath = f'/html/body/div[3]/section/div/div[2]/div/form/table/tbody/tr[2]/td/select[2]/option[{1003-int(end_num)+1}]'
driver.find_element(By.XPATH, xpath).click()
time.sleep(1)

# 조회 버튼 클릭
driver.find_element(By.CSS_SELECTOR, 'a.btn_common.mid.blu').send_keys(Keys.ENTER)

# 번호별 당첨 횟수 출력
stat = {}
print(f'{start_num}~{end_num}회차의 각 번호 별 당첨 횟수...')
for i in range(1, 46):
    xpath = f'/html/body/div[3]/section/div/div[2]/div/table/tbody/tr[{i}]/td[3]'
    content = driver.find_element(By.XPATH, xpath).text
    stat[f'{i}'] = round(int(content)/1003 * 100, 2)
    print(f'{i}번호의 당첨 횟수: {content}')
    time.sleep(1)
# 번호별 당첨 확률 출력
print(f'{start_num}~{end_num}회차의 각 번호 별 당첨 확률...')
for num in stat.keys():
    print(f'{num}번호의 당첨 확률: {stat[num]}%')
# 당첨 확률 정렬 및 상위 6개의 번호 추천
stat = sorted(stat.items(), key= lambda item: item[1], reverse=True)
print('추천 번호는 다음과 같습니다.')
for i in range(6):
    print(f'{stat[i][0]} ', end='')

driver.close()