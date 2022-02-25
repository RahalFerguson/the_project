import opc
import time
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 29
Run = True
while Run:
    for rows in range(6):
        if led < 59:
         leds[led + rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1
         print(led)

        else:
         Run= False
         break

led = 29
Run = True
while Run:
    for rows in range(6):
        if led < 60:
         leds[led - rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1

         print(led)

        else:
         Run= False
         break

led = 30
Run = True
while Run:
    for rows in range(6):
        if led < 59:
         leds[led + rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1
         print(led)

        else:
         Run= False
         break

led = 30
Run = True
while Run:
    for rows in range(6):
        if led < 60:
         leds[led - rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1

         print(led)

        else:
         Run= False
         break

led = 31
Run = True
while Run:
    for rows in range(6):
        if led < 59:
         leds[led + rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1
         print(led)

        else:
         Run= False
         break

led = 31
Run = True
while Run:
    for rows in range(6):
        if led < 60:
         leds[led - rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1

         print(led)

        else:
         Run= False
         break



