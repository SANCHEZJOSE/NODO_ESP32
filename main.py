from machine import Pin,I2C
import SCD30

i2c = I2C(scl=Pin(15), sda=Pin(4), freq=80000)


while true:
  SCD30.initialize()

