#IO0 IO4 IO10 IO12~19 IO21~23 IO25~27

githubProjectURL = 'https://github.com/newton45/Esp32_Testing/blob/master/Testing.txt'

from ota_update.main.ota_updater import OTAUpdater

import urequests
import time
from machine import Pin,PWM
import network
import socket

SSID="CMCC-101"
PASSWORD="101101101"
wlan=None

led=Pin(2,Pin.OUT)        


def start():
  try:
    print('WIFI_Connecting...')
    connectWifi(SSID, PASSWORD)
    while 1:
      led.value(1)
      time.sleep(2)
      led.value(0)
      time.sleep(2)
  except:
    led.deinit()
    wlan.disconnect()
    wlan.active(False)
  
def download_and_install_update_if_available():
   o = OTAUpdater(githubProjectURL)
   o.download_and_install_update_if_available(SSID, PASSWORD)
  
def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  print("WIFI_Connected!")
  return True

def getHttp():
  response = urequests.get('https://raw.githubusercontent.com/newton45/ESP_32/master/test.txt')
  print(response.text)
  led.value(int(response.text))

def boot():
   download_and_install_update_if_available()
   start()
 
boot()