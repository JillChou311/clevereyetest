from selenium.webdriver.common.by import By

package_name = "com.gemteks.litenet"


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


class LoginPageLocators(object):
    ACCOUNT_INFO_TEXTFIELD = (By.CLASS_NAME, "android.widget.EditText")
    SIGNIN_BUTTON = (By.ID, 'com.gemteks.clevereyes:id/login_button_login')


class CameraPageLocators(object):
    CAMERA_TITAL = (By.ID,'com.gemteks.clevereyes:id/tvAbTitle')
    CAMERA_ONLINE_STATUE = (By.ID,'com.gemteks.clevereyes:id/tvDeviceStatus')
    CAMERA_LIVE_VIEW = (By.ID, 'com.gemteks.clevereyes:id/imvCameraIcon')
    DETAIL_TITAL = (By.ID,'com.gemteks.clevereyes:id/title_name')
    BPS_INFO = (By.ID,'com.gemteks.clevereyes:id/tv_bit_rate')
    FPS_INFO = (By.ID,'com.gemteks.clevereyes:id/tv_debug_frame_rate')
    CONNECT_INFO = (By.ID,'com.gemteks.clevereyes:id/tv_error_description')
    CVR_BUTTOM = (By.ID,'com.gemteks.clevereyes:id/btn_cvr_port')
    CAMERA_SETTING = (By.ID,'com.gemteks.clevereyes:id/llMyDeviceManage')

class CVRPageLocators(object):
    PLAY_CVR_BUTTOM = (By.ID,'com.gemteks.clevereyes:id/cvr_timebar_indicator_date')


class CameraManageLocators(object):
    CAMERANAME_TEXTFIELD = (By.ID,'com.gemteks.clevereyes:id/text_device_name')
    CAMERANAME_TEXTFIELD2 = (By.ID,'com.gemteks.clevereyes:id/tvContentSetting8')
    CAMERARENAME_BUTTON = (By.ID,'com.gemteks.clevereyes:id/btnOkSetting8')
    CAMERA_SET = (By.ID,'com.gemteks.clevereyes:id/imvAbAdd')
    CAMERA_SET_TITAL = (By.ID,'com.gemteks.clevereyes:id/tvAbTitle')
    CAMERA_INFO = (By.CLASS_NAME,'android.widget.TextView')


