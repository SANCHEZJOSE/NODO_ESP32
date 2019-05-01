from machine import Pin,I2C
import SCD30.SCD30

i2c = I2C(scl=Pin(15), sda=Pin(4), freq=80000)
SCD30.initialize()


while true:
     result=bytearray(3)
     if scd30.isAvailable() :
          scd30.getCarbonDioxideConcentration(result)
          print("Carbon Dioxide Concentration is: ",result[0],"ppm") 
          print("Temperature: ",result[1], "°C")
          print("Humidity:",result[2],"%")
    time.sleep(2)
  



