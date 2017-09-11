# coding=utf-8

import os
import unittest
import re
import time

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
        os.system('adb -s F8AZCY230515 shell am start -n io.appium.settings/.Settings -e wifi on')
        sleep(50)
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

    # Test script

    def test_1_wifiSet(self):
        elem = self.driver.find_elements_by_id("com.android.settings:id/title")
        for e in elem:
            try:
                aaa = e.text.encode("GBK", 'ignore')
            except Exception, c:
                print c
            m = re.match(r'Wi', aaa)
            if m:
                e.click()
                sleep(2)
                break

        self._ScanSSID("DropAP-0bb068", 'android:id/title', 1000, 200)

        elem = self.driver.find_elements_by_class_name('android.widget.TextView')
        connect_status_fail = True
        for e in elem:
            if e.text == 'Connected':
                connect_status_fail = False
                print 'local already connect.'
                break
            else:
                continue

        if connect_status_fail:
            element = self.driver.find_elements_by_class_name("android.widget.Button")
            for e in element:
                if e.text == 'Connect':
                    e.click()

            sleep(5)
            self._ScanSSID("DropAP-0bb068", 'android:id/title', 1000, 200)
            elem = self.driver.find_elements_by_class_name('android.widget.TextView')
            connect_status = False
            for e in elem:
                if e.text == 'Connected':
                    connect_status = True
                    break
                else:
                    continue
                
            if connect_status:
                sleep(2)
            else:
                timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                self.driver.get_screenshot_as_file("screen"+timestr2+".png")           

            assert connect_status,'Connect to local fail.'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(wifi_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
