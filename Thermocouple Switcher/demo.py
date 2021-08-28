from machine import Pin, I2C
from eeprom import EEPROM

# I2C0 - 0, 4, 8, 12, 16, 20
# I2C1 - 2, 6, 10, 14, 18, 26
sda = Pin(0)

# I2C0 - 1, 5, 9, 13, 17, 21
# I2C1 - 3, 7, 11, 15, 19, 27
scl = Pin(1)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)

print(i2c.scan())

# lcdaddr = 60
# i2c.writeto(lcdaddr, 'text')

# eepromaddr = 80
# eeprom = EEPROM(i2c, i2caddr)

# print(eeprom.read(0, 4096))

# offset = calibration offset between Pico and Ectron
# eeprom.write(0, offset)

# eeprom.wipe()

