from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pyautogui as pag


class Annuity:
    def __init__(self, driver):
        self.__driver = driver

        # 페이지 정보
        self.__annuityUrl = 'https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LP72'

    # 연금복권 구매 페이지 여는 함수
    def OpenAnnuity(self):
        self.__driver.get(self.__annuityUrl)

    # 연금복권 구매 함수
    def BuyAnnuity(self):
        self.__AutoNumClick()
        self.__SelectFinishClick()
        self.__BuyClick()
        self.__CloseAnnuity()

    # 연금복권 구매 페이지에서 자동 번호 선택 버튼을 누르는 함수
    def __AutoNumClick(self):
        autoNumPos = pag.locateCenterOnScreen('./image/AutoNum.png')
        pag.click(autoNumPos)

        # 번호가 입력될 때까지 대기
        while True:
            if pag.locateOnScreen('./image/SelCheck.png') == None:
                print('click auto button')
                break

    # 번호 입력된 후 입력 완료 버튼을 누르는 함수
    def __SelectFinishClick(self):
        selFinPos = pag.locateCenterOnScreen('./image/SelFin.png')
        pag.click(selFinPos)

        # 번호 선택이 완료되어서 페이지 하단에 표시될때까지 대기
        while True:
            if pag.locateOnScreen('./image/Heart.png') != None:
                print('click select finish button')
                break

    # 구매 진행하는 함수
    def __BuyClick(self):
        buyPos = pag.locateCenterOnScreen('./image/Buy.png')
        pag.click(buyPos)

        try:
            WebDriverWait(self.__driver, 1).until(
                expected_conditions.alert_is_present())
            buy2Pos = pag.locateCenterOnScreen('./image/Buy2.png')
            pag.click(buy2Pos)

            # 구매 성공시까지 대기
            while True:
                if pag.locateOnScreen('./image/Close.png'):
                    closePos = pag.locateCenterOnScreen('./image/Close.png')
                    print('purchase success')
                    break

                pag.click(closePos)
                time.sleep(3)
        except:
            print('purchase fail')
            self.__driver.quit()

    # 페이지 종료하는 함수
    def __CloseAnnuity(self):
        self.__driver.quit()
