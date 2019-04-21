# from micropython import constans
from machine import I2C
from constans import *


class SCD30:
    def __init__(self):
        self.devAddr = SCD30_I2C_ADDRESS
    def initialize(self):
        self.i2c = I2C(freq=80000)
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
    
    
    
    def getCarbonDioxideConcentration(self,result):
        buf = bytearray(18) #Un arreglo de 18 elementos de valor 0        
        self.writeCommand(SCD30_READ_MEASUREMENT)
        self.readBuffer(buf)
        co2 = ((buf[0] << 24) | (buf[1] << 16) | (buf[3] << 8) | buf[4])

        temp = ((buf[6] << 24) | (buf[7] << 16) | (buf[9] << 8) | buf[10])

        hum = ((buf[12] << 24) | (buf[13] << 16) | (buf[15] << 8) | buf[16])
        return {"CO_2":co2,"Temperatura":temp,"humedad":hum}   
    
    def writeCommand(self,command):
        self.i2c.start(self.devAddr)
        self.i2c.write(command >> 8) # MSB
        self.i2c.write(command & 0xff) # LSB
        self.i2c.stop()
    
    
    def writeCommandWithArguments(self,command,arguments):
        buf= bytearray(5)
        buf[0] = command >> 8
        buf[1] = command & 0xff
        buf[2] = arguments >> 8
        buf[3] = arguments & 0xff
        checkSum = self.calculateCrc(buf[2:3], 2)
        buf[4] = checkSum
        self.writeBuffer(buf)

    def readRegister(self,address):
        buf= bytearray(2)
        self.writeCommand(address)
        self.readBuffer(buf)
        return (((buf[0]) << 8) | buf[1])
    
    def writeBuffer(self,buf):
        self.i2c.writeto(self.devAddr,buf)
    
    def readBuffer(self,buf):
        self.i2c.readfrom_into(self.devAddr,buf,stop=True)
    
    def calculateCrc(self,data,len):
        crc = 0xff
        # calculates 8-Bit checksum with given polynomial
        for i in range(0,len):
            crc ^= (data[i])
            for i in range(7,-1,-1):
                if(crc & 0x80):
                    crc = (crc << 1) ^ SCD30_POLYNOMIAL
                else: 
                    crc = (crc << 1)
        
        return crc


