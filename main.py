#!/usr/bin/env python3

import os

from AutoConnector import AutoConnector

if __name__ == "__main__":

    a = AutoConnector( os.path.dirname( os.path.abspath(__file__) ) + "/" + "chromedriver", "Chrome" )
    if a.tryToConnect():
        print("Successfully connected")
    else:
        print("Connection failed")
