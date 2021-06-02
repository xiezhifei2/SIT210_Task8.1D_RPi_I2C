import smbus
import time

# Constants taken from the datasheet

DEVICE = 0x23     # Default device I2C address

ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1)

def convertToNumber(data):
    result = (data[1] + (256 * data[0])) / 1.2  # convert 2 bytes of data to decimal
    return (result)

def readLight(addr = DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
    return convertToNumber(data)
try:
    while True:
        
        lightLevel = readLight()
        print('Light Level :' + format(lightLevel,'.2f') + ' lx')
        
        if (lightLevel < 30):
            print('too dark')
        elif (lightLevel >= 30 and lightLevel<=100):
            print('dark')
        elif (lightLevel >100 and lightLevel<=300):
            print('medium')
        elif (lightLevel >300 and lightLevel <=900):
            print('bright')
        elif (lightLevel >= 1000):
            print('too bright')
            
        time.sleep(1.5)
except KeyboardInterrupt:
    print('Hellow world')