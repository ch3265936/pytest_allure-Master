# -*- coding: utf-8 -*-

from page.base_page import BasePage
from setting import Setting as ST

class LoginPage(BasePage):

    def __init__(self):
        self._toLogin = (self.MB.ID, 'com.efund.jqb:id/tv_username')
        self._user = (self.MB.ID, 'com.efund.jqb:id/userName')
        self._delete = (self.MB.ID, 'com.efund.jqb:id/btn_clear_all_for_username')
        # self._av = (self.MB.ID, 'home_bottom_tab_button_contact')
        # self._user = (self.MB.ID, 'home_bottom_tab_button_mine')
     # print('test_something click ------ ')
        # time.sleep(20)
        # self.driver.find_element_by_id(elementPage.toLogin).click()
        # print("进入登入页面")
        # time.sleep(3)
        # self.driver.find_element_by_id(elementPage.userName).click()
        # self.driver.find_element_by_id(elementPage.deleteName).click()
        # self.driver.find_element_by_id(elementPage.userName).send_keys(elementPage.colinAccount.get('userName'))
        # self.driver.find_element_by_id(elementPage.passWord).click()
        # for x in elementPage.colinAccount.get('passWord'):
        #     print("input:" + x)
        #     self.driver.find_element_by_xpath('//*[@text=%s]' % (x)).click()
        #
        # time.sleep(3)
        # self.driver.find_element_by_id(elementPage.login).click()
        # elementPage.assertTag = True
        # if elementPage.assertTag == True:
        #     print("第一条案例执行结果：True")
        # else:
        #     print("第一条案例执行结果：False")

    def switch_tologin(self):
        self.find(self._toLogin).click()
        return
    def switch_cleakUser(self):
        self.find(self._user).click()
        return
    def switch_cleakDelete(self):
        self.find(self._delete).click()
        return
    def input_user(self):
        self.find(self._user).send_keys(ST.Account.get('userName'))