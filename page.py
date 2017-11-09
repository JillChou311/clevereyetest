# coding=utf-8
import time
from element import BasePageElement
from locator import *
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


def singlePageSearch(self, targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    find_the_text = False
    for e in elem:
        if e.text == targetText:
            ssid_elem = e
            ssid_elem.click()
            find_the_text = True
            break
    return find_the_text


def singlePageSearch2(self, targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    find_the_text = False
    count = 0
    for e in elem:
        #       print 'name:'+e.text
        #        print 'count:'+str(count)
        if e.text == targetText:
            ssid_elem = e
            #            print 'name:'+ssid_elem.text
            #            print 'count:'+str(count)
            return ssid_elem, count
            break
        count = count + 1


def singlePageSearch3(self, targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    for e in elem:
        #       print 'name:'+e.text
        if e.text == targetText:
            ssid_elem = e
            #            print 'name:'+ssid_elem.text
            return True
            break
    return False


def checkText(self, targetText, Locators):
    elem = self.driver.find_elements(*Locators)
    find_the_text = False
    e = elem[0]
    if e.text == targetText:
        find_the_text = True
    return find_the_text


def getText(self, element):
    try:
        print element.text
        return True
    except NoSuchElementException:
        return False


class LoginPage(BasePage):
    def send_account_info(self, account, password):
        textfields = self.driver.find_elements(*LoginPageLocators.ACCOUNT_INFO_TEXTFIELD)
        textfields[0].send_keys(account)
        self.driver.press_keycode(4)  # press return
        textfields[1].click()
        textfields[1].send_keys(password)
        self.driver.press_keycode(4)  # press return
        element = self.driver.find_element(*LoginPageLocators.SIGNIN_BUTTON)
        element.click()


class CameraPage(BasePage):

    def click_live_view(self):
        elem = self.driver.find_element(*CameraPageLocators.CAMERA_LIVE_VIEW)
        elem.click()

    def check_my_camera_logo_appear(self):

        for i in range(0,3):
            try:
                element = self.driver.find_element(*CameraPageLocators.CAMERA_TITAL)
            except NoSuchElementException:
                try:
                    element = self.driver.find_element(*LoginPageLocators.SIGNIN_BUTTON)
                    element.click()
                    print 'click login again'
                except NoSuchElementException:
                    if i == 2:
                        print 'wait login for too long'
                        timestr2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
                        self.driver.get_screenshot_as_file("screen" + timestr2 + ".png")
                        print "Pic record on" + "screen" + timestr2 + ".png"
                        return False
                print 'wait 15 sec for login'
                sleep(15)

        try:
            elem = self.driver.find_element(*CameraPageLocators.CAMERA_ONLINE_STATUE)
            if elem.text == u'• 上線':
                return True
            else:
                onLine = False
                for j in range(0,2):
                    element = self.driver.find_element(*CameraPageLocators.REFRESH_PAGE)
                    element.click()
                    for i in range(1,4):
                        sleep(10)
                        print '\nwait 10 sec for camera online'
                        if elem.text == u'• 上線':
                            onLine = True
                            return onLine
                        else:
                            continue
                print 'device offline'
                timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                self.driver.get_screenshot_as_file("screen"+timestr2+".png")
                print "Pic record on"+"screen"+timestr2+".png"
                return False

        except :
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "Pic record on"+"screen"+timestr2+".png"
            return False
    def click_back_button(self):
        element = self.driver.find_element(*CameraPageLocators.BACK_BUTTON)
        element.click()

    def click_tital_for_detail(self):
        element = self.driver.find_element(*CameraPageLocators.DETAIL_TITAL)
        for i in range(1,12):
            element.click()

        try:
            elem = self.driver.find_element(*CameraPageLocators.BPS_INFO)
            elem = self.driver.find_element(*CameraPageLocators.FPS_INFO)
        except NoSuchElementException:
            for i in range(1, 12):
                element.click()
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "Pic record on"+"screen"+timestr2+".png"


    def check_internet_status(self):
        try:
            elem = self.driver.find_element(*CameraPageLocators.CONNECT_INFO)
            print elem.text
            timestr2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen" + timestr2 + ".png")
            print "Pic record on" + "screen" + timestr2 + ".png"
            return True
        except NoSuchElementException:
            return False

    def check_bps_appear(self):
        for i in range(0, 2):
            try:
                elem = self.driver.find_element(*CameraPageLocators.BPS_INFO)
                return True
            except NoSuchElementException:
                print 'wait 15 sec for bps appear'
                sleep(15)
        timestr2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.driver.get_screenshot_as_file("screen" + timestr2 + ".png")
        print "Pic record on" + "screen" + timestr2 + ".png"
        return False

    def check_image_page(self):
        element = self.driver.find_element(*CameraPageLocators.CAMERA_NAME)
        if element.text == 'Autotest01':
            return True
        else:
            return False


    def bps_fps_error(self):
        try:
            elem = self.driver.find_element(*CameraPageLocators.BPS_INFO)
            print elem.text
            elem = self.driver.find_element(*CameraPageLocators.FPS_INFO)
            print elem.text
            return True
        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "Pic record on"+"screen"+timestr2+".png"
            return False

    def click_cvr_page(self):
        elem = self.driver.find_element(*CameraPageLocators.CVR_BUTTOM)
        elem.click()

    def swipe_to_click_camera_set(self):
        self.driver.swipe(669,195,333,195,500)
        elem = self.driver.find_element(*CameraPageLocators.CAMERA_SETTING)
        elem.click()


class CVR_page(BasePage):
    def check_play_buttom_appear(self):
        try:
            elem = self.driver.find_element(*CVRPageLocators.PLAY_CVR_BUTTOM)
            return True

        except NoSuchElementException:
            timestr2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen"+timestr2+".png")
            print "Pic record on"+"screen"+timestr2+".png"
            return False

    def swipe_15_minute(self):
        self.driver.swipe(548,642,548,464,1000)
        timestr2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.driver.get_screenshot_as_file("screen" + timestr2 + ".png")
        print "Pic record on" + "screen" + timestr2 + ".png"

    def click_play_cvr_buttom(self):
#        self.driver.tap([(59,777)], 100)
        elem = self.driver.find_element(*CVRPageLocators.PLAY_CVR_BUTTOM)
        elem.click()

    def click_more_detail(self):
        press = 10
        while press > 0:
            self.driver.tap([(360,99)],100)
            print 'press time:'+str(press)
            press = press - 1

        try:
            elem = self.driver.find_element(*CameraPageLocators.BPS_INFO)
            elem = self.driver.find_element(*CameraPageLocators.FPS_INFO)
        except NoSuchElementException:
            press = 10
            while press > 0:
                self.driver.tap([(360,99)], 100)
                print 'press time:' + str(press)
                press = press - 1
            try:
                elem = self.driver.find_element(*CameraPageLocators.BPS_INFO)
                elem = self.driver.find_element(*CameraPageLocators.FPS_INFO)
            except NoSuchElementException:
                timestr2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
                self.driver.get_screenshot_as_file("screen" + timestr2 + ".png")
                print "Pic record on" + "screen" + timestr2 + ".png"


class Camera_setting_page(BasePage):

    def get_all_camera_info(self):
        elem = self.driver.find_element(*CameraManageLocators.CAMERA_SET)
        elem.click()
        elem = self.driver.find_element(*CameraManageLocators.CAMERA_SET_TITAL)
        elem = self.driver.find_elements(*CameraManageLocators.CAMERA_INFO)

    def check_camera_info(self):
        elem = self.driver.find_elements(*CameraManageLocators.CAMERA_INFO)
        try:
            print elem[1].text + ':' + elem[2].text
            print elem[3].text + ':' + elem[4].text
            print elem[5].text + ':' + elem[6].text
            print elem[7].text + ':' + elem[8].text
            return True
        except:
            timestr2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            self.driver.get_screenshot_as_file("screen" + timestr2 + ".png")
            print "Pic record on" + "screen" + timestr2 + ".png"
            return False

    def rename_camera(self,newname):
        elem = self.driver.find_element(*CameraManageLocators.CAMERANAME_TEXTFIELD)
        elem.click()
        elem = self.driver.find_element(*CameraManageLocators.CAMERANAME_TEXTFIELD2)
        elem.send_keys(newname)
        elem = self.driver.find_element(*CameraManageLocators.CAMERARENAME_BUTTON)
        elem.click()

    def check_new_name(self,newname):
        elem = self.driver.find_element(*CameraManageLocators.CAMERANAME_TEXTFIELD)
        if elem.text == newname:
            return True
        else:
            return False
