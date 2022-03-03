import opc
import time
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0
Run = True
while Run:
    for rows in range(6):
        if led < 30:
         leds[led + rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1
         print(led)

        else:
         Run= False
         break

led = 0
Run = True
while Run:
    for rows in range(6):
        if led < 30:
         leds[led - rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1

         print(led)

        else:
         Run= False
         break

led = 1
Run = True
while Run:
    for rows in range(6):
        if led < 30:
         leds[led + rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1
         print(led)

        else:
         Run= False
         break

led = 1
Run = True
while Run:
    for rows in range(6):
        if led < 30:
         leds[led - rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1

         print(led)

        else:
         Run= False
         break

led = 2
Run = True
while Run:
    for rows in range(6):
        if led < 30:
         leds[led + rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1
         print(led)

        else:
         Run= False
         break

led = 2
Run = True
while Run:
    for rows in range(6):
        if led < 30:
         leds[led - rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1

         print(led)

        else:
         Run= False
         break



