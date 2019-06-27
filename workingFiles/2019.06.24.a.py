sync_code_version = 2019.06.24.a


from machine import Pin,PWM
import time
def run():
	led = Pin(2, Pin.OUT)
	print("Running!!!")
	while 1:
		led.value(1)
		time.sleep(0.5)
		led.value(0)
		time.sleep(0.5)