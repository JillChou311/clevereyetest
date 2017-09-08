# coding=utf-8
import os
import unittest
from selenium import webdriver
from appium import webdriver
import page
from time import sleep
from selenium.common.exceptions import WebDriverException

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LiteNet_test(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
      #  sleep(50)
        desired_caps = {}
##        desired_caps['appPackage'] = 'com.gemteks.clevereyes'
##        desired_caps['appActivity'] = 'com.gemtek.clevereyes.CleverEyesIPCam'
##        desired_caps['platformName'] = 'Android'
##        desired_caps['platformVersion'] = '4.4.3'
##        desired_caps['deviceName'] = '015d321ff553f615'
##        desired_caps['udid'] = '015d321ff553f615'
        
        desired_caps['appPackage'] = 'com.gemteks.clevereyes'
        desired_caps['appActivity'] = 'com.gemtek.clevereyes.CleverEyesIPCam'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'F8AZCY230515'
        desired_caps['udid'] = 'F8AZCY230515'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def test_1_live_view(self):
        login_page = page.LoginPage(self.driver)
        login_page.send_account_info('jill_chou@gemteks.com', '12345678')

        camera_page = page.CameraPage(self.driver)
        assert camera_page.check_my_camera_logo_appear(), 'login fail'

        camera_page.click_live_view()

        if camera_page.check_internet_status():
            result = False
        else:
            result = True
        assert result,'connect fail'

        camera_page.click_tital_for_detail()
        assert camera_page.bps_fps_error(),'Can’t access bps & fps'


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LiteNet_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
