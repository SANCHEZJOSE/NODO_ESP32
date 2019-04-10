from micropython import constans
from constans import *
class SCD30:
  def __init__(self):
    devAddr = SCD30_I2C_ADDRESS;
  def initialize():
    #Set temperature offset。
    #setTemperatureOffset(0);  
    setMeasurementInterval(2) # 2 seconds between measurements
    startPeriodicMeasurment() # start periodic measuments
    #setAutoSelfCalibration(true); # Enable auto-self-calibration
  def setTemperatureOffset(offset):
    writeCommandWithArguments(SCD30_SET_TEMP_OFFSET, offset)


