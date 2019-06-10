## Commented sections below are the original code and my code is the uncommented sections. 

    @staticmethod
    def _build_authorization_token(user, password, namespace=None, gateway=None, **kwargs):
        """ Build the Authorization Header for CAM and Native Security
        """
    #    if namespace:
    #        if gateway:
    #            response = requests.get(gateway, auth=HttpNegotiateAuth())
    #            if not response.status_code == 200:
    #                raise RuntimeError(
    #                    "Failed to authenticate through CAM. Expected status_code 200, received status_code: "
    #                    + str(response.status_code))
    #            elif 'cam_passport' not in response.cookies:
    #                raise RuntimeError(
    #                    "Failed to authenticate through CAM. HTTP response does not contain 'cam_passport' cookie")
    #                token = 'CAMPassport ' + response.cookies['cam_passport']
    #        else:
    #            token = 'CAMNamespace ' + b64encode(
    #                str.encode("{}:{}:{}".format(user, password, namespace))).decode("ascii")
    #    else:
    #        token = 'Basic ' + b64encode(
    #            str.encode("{}:{}".format(user, password))).decode("ascii")

    #;For Production:
    #ClientCAMURI=http://C10PROD.MICRON.COM/ibmcognos/cgi-bin/cognosisapi.dll
	#For Test:
	#ClientCAMURI=http://C10TEST.MICRON.COM/ibmcognos/cgi-bin/cognosisapi.dll
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = r'C:\Users\cthieme\Documents\JUNK\Python Stuff\chromedriver.exe')
        driver.get('http://c10prod.micron.com/ibmcognos/cgi-bin/cognosisapi.dll')
        cookie_dictionary = driver.get_cookie('cam_passport')
        cookie = cookie_dictionary['value']
        driver.close()
        return 'CAMPassport' + ' '  + cookie
