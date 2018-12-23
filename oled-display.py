#!/usr/bin/env python3

import os
import random
import time

import oled_128_64 as oled

def main():
    oled.init()
    oled.setNormalDisplay()
    #oled.setHorizontalMode()

    try:
        while True:
            oled.clearDisplay()
            x = random.randint(1, 5)
            y = random.randint(1, 4)
            oled.setTextXY(x, y)  # row, col
            oled.putString("hello friend")
            time.sleep(2)
    finally:
        oled.clearDisplay()

if __name__ == '__main__':
    exit(main())
