from selenium import webdriver
from pyvirtualdisplay import Display
import subprocess

from nmcli_wrapper import *

class AutoConnector(object):

    def __init__( self, driver_path, driver_type ):
        """
        """

        Display( visible=0, size(1024,768) ).start()

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
                "AEON MALL":                     self.connectViaAEON,
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
        TBD
        """

        return True

    def tryToConnect( self, threshold_signal=60, num_trial=3 ):
        """
        """
        APs = getWifiAPs()
        APs_valid = []
        for AP in APs:
            if int(AP["SIGNAL"]) > threshold_signal and AP["SECURITY"] == "--":
                APs_valid.append( AP )

        for AP in APs_valid:
            if AP["SSID"] in self.APlist:
                for i in range( num_trial ):
                    connectAP( AP["SSID"] )
                    if self.APlist[ AP["SSID"] ]() and self.isConnected():
                        return True
                continue

        return False

    def connectViaStarbucks( self ):
        """
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

if __name__ == "__main__":

    a = AutoConnector( "./chrome_driver", "Chrome" )
    a.tryToConnect()
