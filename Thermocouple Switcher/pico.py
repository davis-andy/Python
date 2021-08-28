'''
from serial.tools import list_ports
import serial, time

picoPorts = list(list_ports.grep('2E8A:0005'))

ports = list_ports.comports()

for _ in picoPorts:
    print(_.device)
    print(_.description)
    print(_.hwid)


'''
'''
# 
# This goes into the Pico
#
from machine import Pin
from time import time, localtime, sleep
from select import select
from sys import stdin

timeDelta = 0
year, month, day, hour, minute, second, wday, yday = 0, 0, 0, 0, 0, 0, 0, 0

def timeNow(timeDelta):
    return (time() + timeDelta)

def checkTimeSyncUSB(timeDelta):
    ch, buffer = '', ''
    while stdin in select([stdin], [], [], 0)[0]:
        ch = stdin.read(1)
        buffer = buffer + ch
        if buffer:
            for i in range(len(buffer)):
                if buffer[i] == 'T':
                    break
            buffer = buffer[i:]
            if buffer[:1] == 'T':
                if buffer[1:11].isdigit():
                    syncTime = int(buffer[1:11])
                    if syncTime > 1609459201:  # Thuesday 1st January 2021 00:00:01
                        timeDelta = syncTime - int(time())
                    else:
                        syncTime = 0
    return timeDelta

led_onboard = Pin(25, Pin.OUT)
lastTime = timeNow(timeDelta)

while True:
    timeDelta = checkTimeSyncUSB(timeDelta)
    correctedRTC = timeNow(timeDelta)

    #
    # every second do the following...
    #
    if correctedRTC != lastTime:
        lastTime = correctedRTC

        if timeDelta == 0:
            for i in range(5):
                led_onboard.toggle()
                sleep(0.03)
            led_onboard.value(0)

        (year, month, day, hour, minute, second, wday, yday) = localtime(correctedRTC)
        correctedRTCstring = '%d-%02d-%02dT%02d:%02d:%02d' % (year, month, day, hour, minute, second)

        #
        # every 5 seconds do the following...
        #
        if (second % 5) == 0:
            print('CorrectedRTC Unix epoch time     :', end='')
            print(correctedRTC)
            print('CorrectedRTC localtime time      :', end='')
            print(localtime(correctedRTC))
            print('CorrectedRTC composite date/time :', end='')
            print(correctedRTCstring)
            print()
            




'''

import serial
from serial.tools import list_ports
import time

picoPorts = list(list_ports.grep("2E8A:0005"))

# ser = serial.Serial(port='COM6', baudrate=9600, parity=serial.PARITY_NONE,
                    # stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)


if not picoPorts:
    print("No Raspberry Pi Pico found")
else:
    pico = picoPorts[0].device
    while True:
        with serial.Serial(pico) as s:
            s.flushInput()
            s.flushOutput()
            # s.write(b'\x03')  # interrupt the currently running code
            # s.write(b'\x03')  # (do it twice to be certain)

            # s.write(b'\x01')  # switch to raw REPL mode & inject code
            # for code in pythonInject:
            #     s.write(bytes(code + '\r\n', 'ascii'))
            #     time.sleep(0.01)

            # time.sleep(0.25)
            # s.write(b'\x04')  # exit raw REPL and run injected code
            # time.sleep(0.25)  # give it time to run (observe the LED pulse)
            reading = s.readline().decode('utf-8')
            print(reading)

            s.flushInput()
            s.flushOutput()
            # s.close()
            time.sleep(5)

'''
for i in range(len(picoPorts)):
    print(i)
    print(picoPorts[i].hwid, end='\t')
    print(picoPorts[i].vid, end='\t')
    print(picoPorts[i].pid, end='\t')
    print(picoPorts[i].location, end='\t')
    print(picoPorts[i].product, end='\t')
    print(picoPorts[i].interface, end='\t')
    print(picoPorts[i].serial_number)
'''

'''

import serial
import serial.tools.list_ports as list_ports
import pyvisa
import machine

rm = pyvisa.ResourceManager()
pico = rm.open_resource('ASRL6::INSTR')



temp_sensor = machine.ADC(4)
temperature = temp_sensor.read_u16()
to_volts = 3.3 / 65535

real_temp = temperature * to_volts
celsius = 27 - (real_temp - 0.706) / 0.001721


print(celsius)
'''
