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


class CleverEyes_test(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
       # sleep(50)
        desired_caps = {}
        # desired_caps['appPackage'] = 'com.gemteks.clevereyes'
        # desired_caps['appActivity'] = 'com.gemtek.clevereyes.CleverEyesIPCam'
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.3'
        # desired_caps['deviceName'] = '015d321ff553f615'
        # desired_caps['udid'] = '015d321ff553f615'
        
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

        if result:
            result = True
        else:
            camera_page.click_back_button()
            if camera_page.check_my_camera_logo_appear():
                camera_page.click_live_view()
                if camera_page.check_internet_status():
                    result = False
                else:
                    result = True
        assert result,'connect fail'
        assert camera_page.check_bps_appear(),'wait too long for video'

        camera_page.click_tital_for_detail()
        assert camera_page.bps_fps_error(),'Can’t access bps & fps'

    def test_2_CVR_review(self):
        login_page = page.LoginPage(self.driver)
        login_page.send_account_info('jill_chou@gemteks.com','12345678')

        camera_page = page.CameraPage(self.driver)
        assert camera_page.check_my_camera_logo_appear(),'login fail'

        sleep(5)
        camera_page.click_live_view()
        camera_page.click_cvr_page()

        cvr_page = page.CVR_page(self.driver)
        sleep(20)
        cvr_page.swipe_15_minute()
        cvr_page.click_play_cvr_buttom()

        if camera_page.check_internet_status():
            result = False
        else:
            result = True

        if result:
            result = True
        else:
            camera_page.click_back_button()
            cvr_page.click_play_cvr_buttom()
            if camera_page.check_internet_status():
                result = False
            else:
                result = True

        assert result, 'connect fail'
        assert camera_page.check_bps_appear(),'wait too long for video'

        cvr_page.click_more_detail()
        assert camera_page.bps_fps_error(), 'Can’t access bps & fps'

    def test_3_Camera_setting(self):
        login_page = page.LoginPage(self.driver)
        login_page.send_account_info('jill_chou@gemteks.com', '12345678')

        camera_page = page.CameraPage(self.driver)
        assert camera_page.check_my_camera_logo_appear(), 'login fail'

        sleep(5)
        camera_page.swipe_to_click_camera_set()
        camera_setting_page = page.Camera_setting_page(self.driver)
        camera_setting_page.rename_camera('Autotest')
        assert camera_setting_page.check_new_name('Autotest'),'rename error'

        camera_setting_page.rename_camera('Autotest01')
        assert camera_setting_page.check_new_name('Autotest01'), 'rename error'

        camera_setting_page.get_all_camera_info()
        assert camera_setting_page.check_camera_info(),'get camera info error'

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CleverEyes_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
