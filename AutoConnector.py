from selenium import webdriver
from pyvirtualdisplay import Display
import subprocess
import os

from nmcli_wrapper import *

class AutoConnector(object):

    def __init__( self, driver_path, driver_type ):
        """
        """

        Display( visible=0, size=(1024,768) ).start()

        if driver_type == "HtmlUnit":
            self.driver = webdriver.HtmlUnit( driver_path )
            self.driver.implicitly_wait( 1 )

        elif driver_type == "Firefox":
            self.driver = webdriver.Firefox( driver_path )
            self.driver.implicitly_wait( 1 )

        elif driver_type == "InternetExplorer":
            self.driver = webdriver.InternetExplorer( driver_path )
            self.driver.implicitly_wait( 1 )

        elif driver_type == "Chrome":
            self.driver = webdriver.Chrome( driver_path )
            self.driver.implicitly_wait( 1 )

        else:
            print( "hoge" )


        self.APlist = {
                "at_STARBUCKS_Wi2":              self.connectViaStarbucks,
                "tullys_Wi-Fi":                  self.connectViaTullys,
                "Komeda_Wi-Fi":                  self.connectViaKomeda,
                "00_MCD-FREE-WIFI":              self.connectViaMcDonald,
                "PRONTO_FREE_Wi-Fi":             self.connectViaPRONTO,
                "7SPOT":                         self.connectViaSevenEleven,
                "LAWSON_Free_Wi-Fi":             self.connectViaLawson,
                "Famima_Wi-Fi":                  self.connectViaFamima,
                "AEON":                          self.connectViaAEON,
                "atPARCO":                       self.connectViaParco,
                "DONKI_Free_Wi-Fi":              self.connectViaDONKI,
                "JR-WEST Free Wi-Fi":            self.connectViaJRWest,
                "JR-Central_FREE":               self.connectViaJRCentral,
                "JR-EAST_FREE_Wi-Fi":            self.connectViaJREAST,
                "Metro_Free_Wi-Fi":              self.connectViaTokyoMetro,
                "Toei_Subway_Free_Wi-Fi":        self.connectViaToeiSubway,
                "KEIO FREE Wi-Fi":               self.connectViaKEIO,
                "KEIKYU FREE Wi-Fi":             self.connectViaKEIKYU,
                "FREE Wi-Fi in Keisei Skyliner": self.connectViaKeiseiSkyliner,
                "KEISEI FREE Wi-Fi":             self.connectViaKEISEI,
                "TOBU_Free_Wi-Fi":               self.connectViaTOBU,
                "SEIBU FREE Wi-Fi":              self.connectViaSEIBU,
                "W-NEXCO Free Wi-Fi":            self.connectViaWNEXCO,
                "C-NEXCO Free Wi-Fi":            self.connectViaCNEXCO,
                "E-NEXCO Free Wi-Fi":            self.connectViaENEXCO,
                "FREE_Wi-Fi_and_TOKYO":          self.connectViaTokyo,
                "KYOTO Wi-Fi":                   self.connectViaKyoto,
                "Osaka_Free_Wi-Fi":              self.connectViaOsaka,
                "Hiroshima_Free_Wi-Fi":          self.connectViaHiroshima
                }

    def isConnected( self ):
        """
        """
        proc = subprocess.run( "ping -w 3 -c 1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )

        if proc.returncode == 0:
            return True
        else:
            return False

    def getValidAPs( self ):
        """
        """
        APs = getWifiAPs()
        APs_valid = []
        for AP in APs:
            if int(AP["SIGNAL"]) > threshold_signal and AP["SECURITY"] == "--":
                APs_valid.append( AP )
        return APs_valid

    def tryToConnect( self, threshold_signal=40, num_trial=3, is_debug=True ):
        """
        """
        APs_valid = self.getValidAPs()

        for AP in APs_valid:
            if is_debug:
                print( " AP[SSID] : " + AP["SSID"] )
            if AP["SSID"] in self.APlist.keys():
                if is_debug:
                    print( "trying to connect : " + AP["SSID"] )
                for i in range( num_trial ):
                    connectAP( AP["SSID"] )
                    if self.APlist[ AP["SSID"] ]() and self.isConnected():
                        return True
                if is_debug:
                    print( "failed to connect : " + AP["SSID"] )
                continue

        return False

    def connectViaSkylark( self ):
        """
        """
        ap_name = ".Wi2_Free_at_"
        url = "https://service.wi2.ne.jp/wi2auth/skylark/index.html"

    def connectViaStarbucks( self ):
        """
        connection function for starbucks coffee
        """
        url_loginpage = "https://service.wi2.ne.jp/wi2auth/at_STARBUCKS_Wi2/index.html" 
        button_next_page_id = "button_next_page"
        button_license_id = "button_accept"

        try:

            self.driver.get( url_loginpage )
            self.driver.find_element_by_id( button_next_page_id ).click()
            self.driver.find_element_by_id( button_license_id ).click()

            return True
        
        except:

            return False

    def connectViaTullys( self ):
        """
        connection function for tullys coffee
        """
        url_loginpage = "https://service.wi2.ne.jp/wi2net/TermsLogin/2/?SSID=f9e049afde477ade57f6f717842623b0"
        button_1st_id = "oc_button_to_kiyaku"
        button_2nd_id = "oc_button_kiyaku_accept"

        try:

            self.driver.get( url_loginpage )
            self.driver.find_element_by_id( button_1st_id ).click()
            self.driver.find_element_by_id( button_2nd_id ).click()

            return True

        except:

            return False

    def connectViaKomeda( self ):
        """
        TBD
        """

        return False

    def connectViaMcDonald( self ):
        """
        TBD
        """

        url = "http://w.mdj.jp/wflogin"

        return False

    def connectViaPRONTO( self ):
        """
        TBD
        """

        return False

    def connectViaSevenEleven( self ):
        """
        TBD
        """
        #url = "http://webapp-ap.7spot.jp/?tmst=1565774997"
        url = "http://webapp-ap.7spot.jp"
        email = "hoge@fuga.com"
        password = "hogefuga"

        try:

            self.driver.get( url )
            self.driver.find_element_by_id( "check_terms" ).click()
            self.driver.find_element_by_id( "check_terms_internet" ).click()
            self.driver.find_element_by_name( "register" ).click()

            # 7SPOT login
            ##
            self.driver.find_element_by_id( "member-type-1" ).click()
            self.driver.find_element_by_id( "email" ).send_keys( email )
            self.driver.find_element_by_id( "password" ).send_keys( password )
            ## ?
            
            # 7id login
            ##
            self.driver.find_element_by_id( "member-type-2" ).click()
            self.driver.find_element_by_id( "email" ).send_keys( email )
            self.driver.find_element_by_id( "password" ).send_keys( password )
            ## ?

            # new account of 7SPOT
            ##
            self.driver.find_element_by_name( "register" ).click()
            ##
            self.driver.find_element_by_name( "email" ).send_keys( email )
            self.driver.find_element_by_id( "sex-1" ).click() 
            self.driver.find_element_by_id( "sex-2" ).click() 
            self.driver.find_element_by_id( "birthday" ).send_keys( "1970" )
            self.driver.find_element_by_name( "password" ).send_keys( password )
            self.driver.find_element_by_name( "password_confirm" ).send_keys( password )
            self.driver.find_element_by_class_name( "btn01" ).click()
            ##
            self.driver.find_element_by_id( "btnSubmit" ).click()
            ## これで狩り回委員として利用できる


        except:

            return False

        return False

    def connectViaLawson( self ):
        """
        TBD
        """

        return False

    def connectViaFamima( self ):
        """
        TBD
        """
        url = "http://app.family-wifi.jp/"
        email = "hoge@fuga.com"
        password = "hogefuga"

        try:

            self.driver.get( url )
            #
            self.driver.find_element_by_id( "agreement" ).click()
            self.driver.find_element_by_id( "goTop" ).click()

            #
            self.driver.find_element_by_id( "acccordion_box_582" ).click()

            #
            ## login
            self.driver.find_element_by_name( "data[Authentication][email]" ).send_keys( email )
            self.driver.find_element_by_name( "data[Authentication][password]" ).send_keys( password )
            self.driver.find_element_by_id( "login_btn" ).click()
            ## ?

            ## register
            self.driver.find_element_by_class_name( "btn_img01" )[2].click()
            ##
            self.driver.find_element_by_id( "agreement" ).click()
            self.driver.find_element_by_id( "goRegister" ).click()
            ##
            self.driver.find_element_by_name( "data[Member][email]" ).send_keys( email )
            self.driver.find_element_by_name( "data[Member][email_confirm_local]" ).send_keys( email.split( "@" )[0] )
            self.driver.find_element_by_name( "data[Member][email_confirm_domain]" ).send_keys( email.split( "@" )[0] )
            self.driver.find_element_by_name( "data[Member][password]" ).send_keys( password )
            self.driver.find_element_by_name( "data[Member][password_confirm]" ).send_keys( password )
            self.driver.find_element_by_id( "MemberSex1" ).click()
            self.driver.find_elements_by_class_name( "btn_img01" )[1].click()
            ##
            self.driver.find_elements_by_id( "btnSubmit" ).click()
            ## ?


        except:

            return False

    def connectViaAEON( self ):
        """
        TBD
        """

        return False

    def connectViaParco( self ):
        """
        TBD
        """

        return False

    def connectViaDONKI( self ):
        """
        TBD
        """

        return False

    def connectViaJRWest( self ):
        """
        TBD
        """

        return False

    def connectViaJRCentral( self ):
        """
        TBD
        """

        return False

    def connectViaJREAST( self ):
        """
        TBD
        """

        return False

    def connectViaTokyoMetro( self ):
        """
        TBD
        """

        return False

    def connectViaToeiSubway( self ):
        """
        TBD
        """

        return False

    def connectViaKEIO( self ):
        """
        TBD
        """

        return False

    def connectViaKEIKYU( self ):
        """
        TBD
        """

        return False

    def connectViaKeiseiSkyliner( self ):
        """
        TBD
        """

        return False

    def connectViaKEISEI( self ):
        """
        TBD
        """

        return False

    def connectViaTOBU( self ):
        """
        TBD
        """

        return False

    def connectViaSEIBU( self ):
        """
        TBD
        """

        return False

    def connectViaWNEXCO( self ):
        """
        TBD
        """

        return False

    def connectViaCNEXCO( self ):
        """
        TBD
        """

        return False

    def connectViaENEXCO( self ):
        """
        TBD
        """

        return False

    def connectViaTokyo( self ):
        """
        TBD
        """

        return False

    def connectViaKyoto( self ):
        """
        TBD
        """

        return False

    def connectViaOsaka( self ):
        """
        TBD
        """

        return False

    def connectViaHiroshima( self ):
        """
        TBD
        """

        return False
