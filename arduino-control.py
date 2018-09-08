import weather
import serial
import sys
import time


def set_led(s, red, yellow):
    if s is None:
        return
    if red or yellow:
        s.write(b'2')
    elif red:
        s.write(b'1')
    elif yellow:
        s.write(b'3')
    else:
        s.write(b'0')


if __name__ == "__main__":
    s = None
    if len(sys.argv) <= 1:
        pass
    else:
        dev = sys.argv[1]
        speed = int(sys.argv[2]) if len(sys.argv) >= 3 else 9600
        s = serial.Serial(dev, speed)

    local = weather.NOAA()

    while True:
        temp = local.temperature()

        if temp >= 75:
            print('HIGH TEMP')
            set_led(s, True, False)
        elif temp >= 60:
            print('MED TEMP')
            set_led(s, True, True)
        else:
            set_led(s, False, True)

        local.update()

        time.sleep(1)
