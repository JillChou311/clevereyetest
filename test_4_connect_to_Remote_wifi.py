# coding=utf-8

import os
import unittest
import re

from selenium import webdriver
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class wifi_test(unittest.TestCase):
    def _ScanSSID(self, ssid, button_id, start_y, end_y):
        scan_result = False
        ssid_elem = None
        for i in range(10):
            elem = self.driver.find_elements_by_id(button_id)
            for e in elem:
                if e.text == ssid:
                    scan_result = True
                    ssid_elem = e
                    break
            if scan_result:
                break
            else:
                self.driver.swipe(200, start_y, 200, end_y, 3000)
        ssid_elem.click()

    # initialize

    def setUp(self):

        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': 'F8AZCY230515',
            'appPackage': 'com.android.settings',
            'appActivity': 'Settings'
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # Cleaning up
    def tearDown(self):
        sleep(2)
        self.driver.quit()


    def test_1_wifi_closed(self):
        os.system('adb -s F8AZCY230515 shell am start -n io.appium.settings/.Settings -e wifi off')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(wifi_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
