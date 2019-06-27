
sync_code_version = '2019.06.27.a'


from machine import Pin,PWM
import time

pwm =PWM(Pin(2),100)
FPS = 60
timeGap_ms = 1000/FPS

def runSync():
	led = Pin(2, Pin.OUT)
	print("Running!!!")
	
	saveFile = open('1.txt', 'r')
  while 1:
    for line in saveFile:
      t1 = time.ticks_ms()
      v = int(line)*4
      pwm.duty(v)
      t = 0
      while t<timeGap_ms:
        t2 = time.ticks_ms()
        t = time.ticks_diff(t1, t2)



