import machine
import time

def blink(pin=15, blink_time=500):
    """ Blink a specific led for a defined cycle
    """
    pin = machine.Pin(pin, machine.Pin.OUT)

    if pin.value() == 1:
        pin.off()

    pin.on()
    time.sleep_ms(blink_time)
    pin.off()


def blinking(quantity=4, blink_ms=100):
    """ Blink multiple times with sleep between blinks
    """
    for qty in range(quantity):
        print(qty)
        blink()
        time.sleep_ms(blink_ms)


blinking(20)