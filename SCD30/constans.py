#Registros
SCD30_I2C_ADDRESS                      = const(0x61)

SCD30_CONTINUOUS_MEASUREMENT           = const(0x0010)
SCD30_SET_MEASUREMENT_INTERVAL         = const(0x4600)
SCD30_GET_DATA_READY                   = const(0x0202)
SCD30_READ_MEASUREMENT                 = const(0x0300)
SCD30_STOP_MEASUREMENT                 = const(0x0104)
SCD30_AUTOMATIC_SELF_CALIBRATION       = const(0x5306)
SCD30_SET_FORCED_RECALIBRATION_FACTOR  = const(0x5204)
SCD30_SET_TEMPERATURE_OFFSET           = const(0x5403)
SCD30_SET_ALTITUDE_COMPENSATION        = const(0x5102)
SCD30_READ_SERIALNBR                   = const(0xD033)

SCD30_SET_TEMP_OFFSET                  = const(0x5403)


SCD30_POLYNOMIAL                       = const(0x31) #P(x) = const(x^8 + x^5 + x^4 + 1 = const(100110001