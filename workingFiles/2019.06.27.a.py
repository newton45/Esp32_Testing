sync_code_version = '2019.06.27.a'


from machine import Pin,PWM
import time
def run():
	led = Pin(2, Pin.OUT)
	print("Running!!!")
	
	led.value(1)
	time.sleep(0.5)
	led.value(0)
	time.sleep(0.5)
	led.value(1)
	time.sleep(0.5)
	led.value(0)
	time.sleep(0.5)
	led.value(1)
	time.sleep(0.5)
	led.value(0)
	time.sleep(0.5)
	led.value(1)
	time.sleep(0.5)
	led.value(0)
	time.sleep(0.5)