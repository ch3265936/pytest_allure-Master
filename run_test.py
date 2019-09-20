# -*- coding: utf-8 -*-
from multiprocessing import Process

import pytest

from service.server import Server
from setting import Setting
from utils.ope_run_data import OpeRunData


def run_test_action(index):
    Setting.UDID = OpeRunData().get_value(f'device_{index}', 'udid')
    Setting.PORT = OpeRunData().get_value(f'device_{index}', 'port')
    Setting.Account =Setting.zpjAccount  #选择账号(多设备同账号 多设备多账号 IF判断)
    pytest.main( ['-s', '-q', '--alluredir', './report/xml', 'test_app/'])

if __name__ == '__main__':
    s = Server()
    s.start_appium_server()

    for i in range(len(s.device_list)):
        p = Process(target=run_test_action, args=(i,))
        p.start()
        p.join()
