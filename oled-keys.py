#!/usr/bin/env python3

import os
import select

from enum import Enum

class GPIO(Enum):
    D0 = 0
    D1 = 1
    D2 = 2

class Edge(Enum):
    RISING = "rising"
    FALLING = "falling"

def init_gpio(gpio, edge):
    # export to userspace
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(gpio.value) + "\n")

    gpio_path = "/sys/class/gpio/gpio{}".format(gpio.value)
    # set direction
    with open(gpio_path + "/direction", "w") as f:
        f.write("in\n")

    # set edge
    with open(gpio_path + "/edge", "w") as f:
        f.write(edge.value + "\n")

    return os.open(gpio_path + "/value", os.O_RDWR | os.O_NONBLOCK);

def release_gpio(gpio):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(gpio.value) + "\n");

def main():
    pins = [GPIO.D0, GPIO.D1, GPIO.D2]
    fds = [init_gpio(pin, Edge.RISING) for pin in pins]

    epoll = select.epoll()
    for fd in fds:
        epoll.register(fd, select.EPOLLET)

    try:
        while True:
            events = epoll.poll(3)
            print("Got events: {}\n".format(events))
            
    finally:
        for fd in fds:
            epoll.unregister(fd)
        epoll.close()
        for pin in pins:
            release_gpio(pin)

if __name__ == '__main__':
    exit(main())
