#!/usr/bin/env python

import opc
import time

led_colour=[(260,100,0)]*180

client = opc.Client('localhost:7890')

print (enumerate(led_colour))
for item in enumerate(led_colour):
    time.sleep(0.2)
    print (item)
    if item[0]%2 == 0:
        #need to get values out of tuple
        r, g, b = item[1]
        r= r-50

    if item[0]%1 == 0:
        
        r, g, b = item[1]
        r= r-100
        


        #create changed tuple (uses some values from old and some new) 
        new_colour =(r,g,b)
        led_colour[item[0]]= new_colour
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

client.put_pixels(led_colour)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
client.put_pixels(led_colour)
print (led_colour)
