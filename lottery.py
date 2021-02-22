from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class Lottery:
    def __init__(self):
        self.lotteryUrl = 'https://dhlottery.co.kr/user.do?method=login'

        # 에러 로그 제거
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])

        # 크롬 드라이버 실행 및 동행복권 페이지 열기
        self.driver = webdriver.Chrome(
            './driver/chromedriver.exe', options=self.options)

        self.driver.get(self.lotteryUrl)

        # 로그인 화면 정보 수집
        self.userIdEdit = self.driver.find_element_by_xpath(
            '//*[@id="userId"]')
        self.userPwEdit = self.driver.find_element_by_xpath(
            '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/input[2]')
        self.loginBtn = self.driver.find_element_by_xpath(
            '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a')

        # user 정보 parsing
        self.userId = self.ReadUserInfo()[0]
        self.userPw = self.ReadUserInfo()[1]

    def ReadUserInfo(self):
        userInfo = []
        userFile = open('./user/user.txt', 'r')

        lines = userFile.readlines()

        for line in lines:
            userInfo.append(line.split(':')[1].strip())

        userFile.close()

        return userInfo

    # 로그인 성공 후, 팝업 창이 뜨는 경우 제거하는 함수
    def ClosePopUp(self):
        print('close popup')
        handles = self.driver.window_handles
        mainHandle = self.driver.current_window_handle

        for i in range(len(handles)):
            if handles[i] != mainHandle:
                self.driver.switch_to_window(handles[i])
                self.driver.close()

        self.driver.switch_to_window(mainHandle)

    # 로그인 함수
    def Login(self):
        self.userIdEdit.send_keys(self.userId)
        self.userPwEdit.send_keys(self.userPw)
        self.loginBtn.click()

        try:
            WebDriverWait(self.driver, 1).until(
                expected_conditions.alert_is_present())
            print('login fail')
            self.driver.quit()
        except:
            print('login success')

            if len(self.driver.window_handles) > 0:
                self.ClosePopUp()

    def GetDriver(self):
        return self.driver
