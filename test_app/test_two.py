# -*- coding: utf-8 -*-
import time
from page.page_login import LoginPage



def test_login2(init_test):
    print("222222222222")
    time.sleep(20)
    loginPage = LoginPage()
    loginPage.switch_tologin()
    time.sleep(3)
    loginPage.switch_cleakUser()
    loginPage.switch_cleakDelete()
    time.sleep(3)
    loginPage.input_user()
    time.sleep(3)


