from selenium import webdriver
import subprocess

def getWifiAPs( ):
    """
    """
    fieldnames = [ "NAME"
                  ,"SSID"
                  ,"SSID-HEX"
                  ,"BSSID"
                  ,"MODE"
                  ,"CHAN"
                  ,"FREQ"
                  ,"RATE"
                  ,"SIGNAL"
                  ,"BARS"
                  ,"SECURITY"
                  ,"WPA-FLAGS"
                  ,"RSN-FLAGS"
                  ,"DEVICE"
                  ,"ACTIVE"
                  ,"IN-USE"
                  ,"DBUS-PATH" ]

    command = "LANG=C && nmcli -f "
    for field in fieldnames:
        command += field + ","
    command = command[:-1] + " dev wifi"

    subprocess.run( "LANG=C && nmcli dev wifi rescan", shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )

    proc = subprocess.run( command, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    outputs = proc.stdout.decode("utf8").splitlines()
    title = outputs[0]
    indexes = []
    for field in fieldnames:
        indexes.append( title.index( field ) )

    APs = []
    for line in outputs[1:]:
        AP = {}
        for i, field in enumerate(fieldnames):
            if i != len( fieldnames )-1:
                AP[field] = line[ indexes[i]:indexes[i+1] ].strip()
            else:
                AP[field] = line[ indexes[i]: ].strip()
        APs.append( AP )

    return APs

def connectAP( SSID ):
    """
    """
    proc = subprocess.run( "nmcli dev wifi connect " + SSID, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )

    return True
