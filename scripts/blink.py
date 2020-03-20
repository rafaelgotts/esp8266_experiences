import machine
import time

def blink(pin=16, blink_time=500):
    """ Blink a specific led for a defined cycle
    """
    pin = machine.Pin(pin, machine.Pin.OUT)

    led_on = pin.value() == 0
    if led_on:
        pin.high()

    pin.low()
    time.sleep_ms(blink_time)
    pin.high()


def blinking(quantity=4, blink_ms=100):
    """ Blink multiple times with sleep between blinks
    """
    for qty in range(quantity):
        print(qty)
        blink()
        time.sleep_ms(blink_ms)


blinking(20)