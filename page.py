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
        textfields[1].send_keys(password)

        element = self.driver.find_element(*LoginPageLocators.SIGNIN_BUTTON)
        element.click()


class CameraPage(BasePage):

    def click_live_view(self):
        elem = self.driver.find_element(*CameraPageLocators.CAMERA_LIVE_VIEW)
        elem.click()

    def check_my_camera_logo_appear(self):
        try:
            element = self.driver.find_element(*CameraPageLocators.CAMERA_TITAL)
            elem = self.driver.find_element(*CameraPageLocators.CAMERA_ONLINE_STATUE)
            if elem.text == u'• online':
                return True
            else:
                onLine = False
                for j in range(0,2):
                    element = self.driver.find_element(*CameraPageLocators.REFRESH_PAGE)
                    element.click()
                    for i in range(1,4):
                        sleep(10)
                        print '\nwait 10 sec'
                        if elem.text == u'• online':
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

#
#
# class RegisterPage(BasePage):
#     def send_account(self, account):
#         textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
#         textfields[0].send_keys(account)
#         self.driver.press_keycode(66)  # enter key
#         textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
#
#     def send_password(self, password):
#         textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
#         textfields[1].send_keys(password)
#         self.driver.press_keycode(66)  # enter key
#
#     def send_password_confirm(self, password_confirm):
#         textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
#         textfields[2].send_keys(password_confirm)
#         self.driver.press_keycode(66)  # enter key
#         self.driver.press_keycode(4)  # press return
#
#     def click_send_button(self):
#         Send = self.driver.find_element(*RegisterPageLocators.SEND_BUTTON)
#         Send.click()
#
#     def check_error_message(self, targetText):
#         return checkText(self, targetText, RegisterPageLocators.ERROR_MESSAGE_TEXT)
#
#     def send_account_info(self, account, password, password_confirm):
#         textfields = self.driver.find_elements(*RegisterPageLocators.ACCOUNT_INFO_TEXTFIELD)
#         textfields[0].send_keys(account)
#         textfields[1].send_keys(password)
#         textfields[2].send_keys(password_confirm)
#         self.driver.press_keycode(4)  # press return
#         Send = self.driver.find_element(*RegisterPageLocators.SEND_BUTTON)
#         Send.click()
#
#
# class RegionPage(BasePage):
#     def add_new_region(self, regionName):
#         selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
#         selectPath.click()
#         element = self.driver.find_element(*RegionPageLocators.ADD_NEW_REGION_BUTTON)
#         element.click()
#         element = self.driver.find_element(*RegionPageLocators.REGION_NAME_TEXTFILED)
#         element.send_keys(regionName)
#         element = self.driver.find_element(*RegionPageLocators.SAVE_NEW_NAME_BUTTON)
#         element.click()
#
#     def edit_region(self, regionName, editName):
#         selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
#         selectPath.click()
#         singlePageSearch(self, regionName, RegionPageLocators.SELECT_REGION)
#         element = self.driver.find_elements(*RegionPageLocators.EDIT_REGION_NAME_BUTTON)
#         element[2].click()  ##chaaaaangggeeee aaagain
#         length = len(regionName)
#         element = self.driver.find_element(*RegionPageLocators.REGION_NAME_TEXTFILED)
#         element.click()
#         while length > 0:
#             self.driver.press_keycode(67)  # press del
#             length = length - 1
#         element.send_keys(editName)
#         element = self.driver.find_element(*RegionPageLocators.SAVE_NEW_NAME_BUTTON)
#         element.click()
#
#     def check_out_region(self, regionName):
#         selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
#         selectPath.click()
#         return singlePageSearch(self, regionName, RegionPageLocators.SELECT_REGION)
#
#     def delete_region(self, regionName):
#         selectPath = self.driver.find_element(*RegionPageLocators.SELECT_PATH_BUTTON)
#         selectPath.click()
#         action = TouchAction(self.driver)
#         singlePageSearch(self, regionName, RegionPageLocators.SELECT_REGION)
#         element = self.driver.find_elements(*RegionPageLocators.EDIT_REGION_NAME_BUTTON)
#         action.long_press(element[2]).perform()
#         element = self.driver.find_elements(*RegionPageLocators.CANCEL_BUTTON)
#         element[1].click()
#         sleep(5)
#
#
# class ScenePage(BasePage):  ## CANT CONFIRM
#     def add_new_scene(self, regionName):
#         element = self.driver.find_element(*ScenePageLocators.ADD_NEW_SCENE_BUTTON)
#         element.click()
#
#         element = self.driver.find_element(*ScenePageLocators.SCENE_NAME_TEXTFILED)
#         element.send_keys(regionName)
#         element = self.driver.find_element(*ScenePageLocators.SAVE_NEW_NAME_BUTTON)
#         element.click()
#
#         self.driver.tap([(341, 843), ])
#
#     ##        element = self.driver.find_element(*ScenePageLocators.CONFIRM_SAVE_BUTTON)
#     ####        element = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]')
#     ##        element.click()
#
#
#     def edit_scene(self, regionName, editName):
#         singlePageSearch(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
#         length = len(regionName)
#         element = self.driver.find_element(*ScenePageLocators.SCENE_NAME_TEXTFILED)
#         element.click()
#         while length > 0:
#             self.driver.press_keycode(67)  # press del
#             length = length - 1
#         element.send_keys(editName)
#         element = self.driver.find_element(*ScenePageLocators.SAVE_EDIT_SCENE_NAME_BUTTON)
#         element.click()
#
#         self.driver.tap([(341, 843), ])
#
#     ##        element = self.driver.find_element(*ScenePageLocators.CONFIRM_SAVE_BUTTON)
#     ##        element.click()
#
#     def check_out_scene(self, regionName):
#         #        singlePageSearch2(self, regionName, ScenePageLocators.SCENE_NAME_TEXTFILED)
#         return singlePageSearch3(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
#
#     def delete_scene(self, regionName):
#         action = TouchAction(self.driver)
#         #        singlePageSearch2(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
#         element, position = singlePageSearch2(self, regionName, ScenePageLocators.SCENE_NAME_TEXT)
#         action.long_press(element).perform()
#         element2 = self.driver.find_elements(*ScenePageLocators.CANCEL_BUTTON)
#         element2[position - 1].click()
#         sleep(5)
#
#
# class BindingPage(BasePage):
#     def send_binding_info(self, deviceName, pinCode, macNumber):
#         textfields = self.driver.find_elements(*BindingPageLocators.ACCOUNT_INFO_TEXTFIELD)
#         textfields[0].send_keys(deviceName)
#         textfields[1].send_keys(pinCode)
#         textfields[2].send_keys(macNumber)
#         self.driver.press_keycode(4)  # press return
#
#     def click_send_button(self):
#         element = self.driver.find_element(*BindingPageLocators.SEND_BUTTON)
#         element.click()
#
#
# class SettingPage(BasePage):
#     def unbinding_device(self):
#         element = self.driver.find_element(*SettingPageLocators.DEVICE_MANAGEMENT_BUTTON)
#         element.click()
#         element = self.driver.find_element(*DeviceManagementPageLocators.DEVICE_SETTING)
#         element.click()
#         element = self.driver.find_element(*DeviceManagementPageLocators.UNBINDING_DEVICE)
#         element.click()
#         element = self.driver.find_element(*DeviceManagementPageLocators.CONFIRM_UNBINDING_DEVCE)
#         element.click()
#
#     def logout(self):
#         element = self.driver.find_element(*SettingPageLocators.LOGOUT_BUTTON)
#         element.click()
#         element = self.driver.find_element(*SettingPageLocators.LOGOUT_CONFIRM)
#         element.click()
#
#     def check_login_name(self, loginName):
#         loginName = u'設定 (' + loginName + u')'
#         return checkText(self, loginName, SettingPageLocators.UPPER_BANNER)
#
#
#
#
# class BottomBanner(BasePage):
#     def click_bottom_button(self, button_name):
#         if button_name == '保全':
#             number = 0
#         elif button_name == '智慧家電':
#             number = 1
#         elif button_name == '區域':
#             number = 2
#         elif button_name == '情境':
#             number = 3
#         elif button_name == '設定':
#             number = 4
#         textfields = self.driver.find_elements(*BottomBannerLocators.BOTTOM_BANNER)
#         textfields[number].click()
#
#

