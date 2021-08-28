import machine
import utime
import oled

# I2C0 pins: 0,1 / 4,5 / 8,9 / 12,13 / 16,17 / 20,21
# I2C1 pins: 2,3 / 6,7 / 10,11 / 14,15 / 18,19 / 26,27
i2c1 = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
# i2c2 = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))

oled_width = 128
oled_height = 64
oled = oled.SSD1306_I2C(oled_width, oled_height, i2c1)

which_relay = 1

temp_sensor = machine.ADC(4)
conversion = 3.3 / (1 << 12)  # 65535

button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
curr_value = button.value()

adc_volt = temp_sensor.read_u16()
real_volt = adc_volt * conversion
temperature = 27 - ((real_volt - 0.706) / 0.001721)  # 27°C is 0.706V, slope of -1.721mV per degree


def button_handler(pin):
    global which_relay
    global curr_value
    global conversion

    adcvolt = temp_sensor.read_u16()
    realvolt = adcvolt * conversion
    temper = 27 - ((realvolt - 0.706) / 0.001721)

    active = 0
    while active < 10:
        if pin.value() != curr_value:
            active += 1
        else:
            active = 0
        utime.sleep(0.01)

    if which_relay == 1:
        which_relay = 2
        oled.fill(0)
        oled.show()
        relays = 'Relay {} ON'.format(which_relay)
        # tempers = 'Current Temp: {}'.format(temperature)
    elif which_relay == 2:
        which_relay = 3
        oled.fill(0)
        oled.show()
        relays = 'Relay {} ON'.format(which_relay)
        # tempers = 'Current Temp: {}'.format(temperature)
    elif which_relay == 3:
        which_relay = 4
        oled.fill(0)
        oled.show()
        relays = 'Relay {} ON'.format(which_relay)
        # tempers = 'Current Temp: {}'.format(temperature)
    else:
        which_relay = 1
        oled.fill(0)
        oled.show()
        relays = 'Relay {} ON'.format(which_relay)
        # tempers = 'Current Temp: {}'.format(temperature)
    oled.text(relays, 0, 0)
    oled.text('Current Temp:', 0, 10)
    oled.text(str(temper), 0, 20)
    oled.show()


text = 'Relay {} ON'.format(which_relay)
oled.text(text, 0, 0)
oled.text('Current Temp:', 0, 10)
oled.text(str(temperature), 0, 20)
oled.show()
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
