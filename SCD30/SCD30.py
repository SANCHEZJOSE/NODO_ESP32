# from micropython import constans
from machine import I2C
from constans import *
from numpy import * 

class SCD30:
    def __init__(self):
        devAddr = SCD30_I2C_ADDRESS
    def initialize(self):
        #Set temperature offset
        #setTemperatureOffset(0);  
        self.setMeasurementInterval(2) # 2 seconds between measurements
        self.startPeriodicMeasurment() # start periodic measuments
        #setAutoSelfCalibration(true); # Enable auto-self-calibration
    def setTemperatureOffset(self, offset):
        self.writeCommandWithArguments(SCD30_SET_TEMP_OFFSET, offset)

    def isAvailable(self):
        return self.readRegister(SCD30_GET_DATA_READY)

    def setAutoSelfCalibration(self, enable):
        if(enable):
            self.writeCommandWithArguments(SCD30_AUTOMATIC_SELF_CALIBRATION, 1) #Activate continuous ASC
        else: 
            self.writeCommandWithArguments(SCD30_AUTOMATIC_SELF_CALIBRATION, 0) #Deactivate continuous ASC

    def setMeasurementInterval(self, interval):
        self.writeCommandWithArguments(SCD30_SET_MEASUREMENT_INTERVAL, interval)

    def startPeriodicMeasurment(self):
        self.writeCommandWithArguments(SCD30_CONTINUOUS_MEASUREMENT, 0x0000)

    def stopMeasurement(self):
        self.writeCommand(SCD30_STOP_MEASUREMENT)
    
    
    """
    def getCarbonDioxideConcentration(*result)  #<----- PUNTEROOO (?)
      buf = zeros(18);  #Un arreglo de 18 elementos de valor 0
      co2U32 = 0
      tempU32 = 0
      humU32 = 0
      co2Concentration = 0
      temperature = 0
      humidity = 0
      
      writeCommand(SCD30_READ_MEASUREMENT)
      readBuffer(buf, 18)
      
      co2U32 = (uint32_t)((((uint32_t)buf[0]) << 24) | (((uint32_t)buf[1]) << 16) | (((uint32_t)buf[3]) << 8) | ((uint32_t)buf[4]))

      tempU32 = (uint32_t)((((uint32_t)buf[6]) << 24) | (((uint32_t)buf[7]) << 16) | (((uint32_t)buf[9]) << 8) | ((uint32_t)buf[10]))

      humU32 = (uint32_t)((((uint32_t)buf[12]) << 24) | (((uint32_t)buf[13]) << 16) | (((uint32_t)buf[15]) << 8) | ((uint32_t)buf[16]))

      memcpy(&result[0], &co2U32, sizeof(co2Concentration))  
      memcpy(&result[1], &tempU32, sizeof(temperature))    
      memcpy(&result[2], &humU32, sizeof(humidity))    
    """
    def writeCommand(command):
        I2C.start(devAddr)
        I2C.write(command >> 8); # MSB ##????????????????????????
        I2C.write(command & 0xff) # LSB
        I2C.stop()
    
    """
    def writeCommandWithArguments(command,arguments):
      checkSum, buf[5] = { 0 }
      
      buf[0] = command >> 8;
      buf[1] = command & 0xff;
      buf[2] = arguments >> 8;
      buf[3] = arguments & 0xff;
      checkSum = calculateCrc(&buf[2], 2);
      buf[4] = checkSum;
      
      writeBuffer(buf, 5);
      """
    def readRegister(address)
        buf= zeros(2)
        writeCommand(address)
        readBuffer(buf, 2)
        return ((((uint16_t)buf[0]) << 8) | buf[1])  #<-- ??????????
    
    def calculateCrc(self,data,len)
        self.bit=0, self.crc = 0xff
        # calculates 8-Bit checksum with given polynomial
        for i in range (0,len):
            crc ^= (data[i])
            
        for(bit = 8; bit > 0; -- bit)
        
            if(crc & 0x80) crc = (crc << 1) ^ SCD30_POLYNOMIAL;
            else crc = (crc << 1)
        
        
        
        return crc;
