# Blinking Program

# incorporate/include modules
import machine #module with all the microcontroller stuff
import time #module with time methods

# make the LED object
# green LED is GPIO pin 0
led = machine.Pin(0, machine.Pin.OUT)

# Infinite Loop
while True:
  led.value(1) #turn on the LED
  time.sleep(0.25) #wait 0.25 seconds
  led.value(0) #turn off the LED
  time.sleep(0.25) #wait 0.25 seconds

  