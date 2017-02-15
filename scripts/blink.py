import machine
import time

def blink(pin=16, blink_time=100):
    """ Blink a specific led for a defined cycle
    """
    pin = machine.Pin(pin, machine.Pin.OUT)

    if pin.value == 1:
        pin.low()

    pin.high()
    time.sleep_ms(blink_time)
    pin.low()


def blinking(quantity=4, blink_ms=100):
    """ Blink multiple times with sleep between blinks
    """
    for qty in range(quantity):
        print(qty)
        blink()
        time.sleep_ms(blink_ms)
