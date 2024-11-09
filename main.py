import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import _thread


I2C_ADDR = 0x27
totalRows = 4
totalColumns = 20

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

arrow_left = bytearray([0x00,0x00,0x04,0x08,0x1F,0x08,0x04,0x00])
lcd.custom_char(0,arrow_left)


button1 = Pin(2, Pin.IN)
button2 = Pin(4, Pin.IN)

led1 = Pin(12, Pin.OUT)
led2 = Pin(27, Pin.OUT)

arrow_right = bytearray([  0x00,
  0x00,
  0x04,
  0x02,
  0x1F,
  0x02,
  0x04,
  0x00])
lcd.custom_char(1,arrow_right)

clock_simbol = bytearray([
      0x00,
  0x00,
  0x1F,
  0x15,
  0x17,
  0x11,
  0x1F,
  0x00])

lcd.custom_char(2,clock_simbol)

lcd.clear()

lcd.move_to(0,0)

def Arranque():
    led1.off()
    led2.off()
    
    sleep(0.5)
    lcd.move_to(0,0)
    lcd.putchar(chr(0))
    lcd.move_to(19,0)
    lcd.putchar(chr(1))
    lcd.move_to(2,0)
    lcd.putchar(chr(2))
    led1.on()
    led2.on()
    
    sleep(2)
    
    led1.off()
    led2.off()
    lcd.move_to(0,0)
    lcd.putchar(" ")
    lcd.move_to(19,0)
    lcd.putchar(" ")
    lcd.move_to(2,0)
    lcd.putchar(" ")

Arranque()
print("Arranque completado")

#threads:



def thread1():
    while True:
        sleep(0.2)
        v = button1.value()
        if v == 1:
            sleep(0.2)
            led1.on()
            lcd.move_to(19,0)
            lcd.putchar(chr(1))
            sleep(0.2)
            led1.off()
            lcd.move_to(19,0)
            lcd.putchar(" ")
        else:
            led1.off()

def thread2():
    while True:
        sleep(0.2)
        v = button2.value()
        if v == 1:
            sleep(0.2)
            led2.on()
            lcd.move_to(0,0)
            lcd.putchar(chr(0))
            sleep(0.2)
            led2.off()
            lcd.move_to(0,0)
            lcd.putchar(" ")
        else:
            led2.off()

_thread.start_new_thread(thread1, ())
_thread.start_new_thread(thread2, ())

def comm():
    sleep(0.2)
    led1.on()
    lcd.move_to(0,0)
    lcd.putchar(chr(0))
    sleep(0.2)
    led1.off()
    lcd.move_to(0,0)
    lcd.putchar(" ")
    lcd.move_to(0,0)
    lcd.putchar(chr(0))
    lcd.move_to(19,0)
    lcd.putchar(chr(1))
    sleep(0.2)
    lcd.move_to(0,0)
    lcd.putchar(" ")
    lcd.move_to(19,0)
    lcd.putchar(" ")
    sleep(0.2)