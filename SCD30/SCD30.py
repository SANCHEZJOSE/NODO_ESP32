from micropython import constans
from constans import *
class SCD30:
  def __init__(self):
    devAddr = SCD30_I2C_ADDRESS
  def initialize():
    #Set temperature offset。
    #setTemperatureOffset(0);  
    setMeasurementInterval(2) # 2 seconds between measurements
    startPeriodicMeasurment() # start periodic measuments
    #setAutoSelfCalibration(true); # Enable auto-self-calibration
  def setTemperatureOffset(offset):
    writeCommandWithArguments(SCD30_SET_TEMP_OFFSET, offset)
  def isAvailable():
   return readRegister(SCD30_GET_DATA_READY)
  def setAutoSelfCalibration(enable):
    if(enable):
      writeCommandWithArguments(SCD30_AUTOMATIC_SELF_CALIBRATION, 1) #Activate continuous ASC
    else: 
      writeCommandWithArguments(SCD30_AUTOMATIC_SELF_CALIBRATION, 0) #Deactivate continuous ASC
  def setMeasurementInterval(interval):
      writeCommandWithArguments(SCD30_SET_MEASUREMENT_INTERVAL, interval)
  def startPeriodicMeasurment():
     writeCommandWithArguments(SCD30_CONTINUOUS_MEASUREMENT, 0x0000)
  def stopMeasurement():
     writeCommand(SCD30_STOP_MEASUREMENT)
  def getCarbonDioxideConcentration(*result)  #<----- PUNTEROOO (?)


