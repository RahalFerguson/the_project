import opc
import time
import random
leds = [(0,0,0)]*360 #white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
fade_amount = 10
#for led in leds: # pick out an element: led = (255,255,255)
for led in range(30): #pick out indeces: led = 0,1,2,3...
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)



    leds[59-led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)

    led = led + 1 #or reverse if you want
#led = 59
#while led>=0:

#    leds[led] = (0,255,0)
#    time.sleep(.1)
#    client.put_pixels(leds)
#    led = led - 1 #or reverse if you want

led = 0
while led<30: #scroll all rows at the same time
    for rows in range(1,3):
        leds[led + rows*60] = (0,0,255)
    for rows in range(1,3):
        leds[59-led + rows*60] = (0,0,255)
    #leds[led+  0] = (0,0,255) #row 1 - 0-60
    #leds[led+ 60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
    #leds[led+120] = (0,0,255)
    #leds[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
    #leds[led+240] = (0,0,255)
    #leds[led+300] = (0,0,255)
    for rows in range(1,3): #first three rows left to right
        leds[led + rows*60] = (0,100,0)
    for rows in range(3,6): #last three rows reversed (right to left)
        leds[59-led + rows*60] = (250,100,255)
    for rows in range(3,6):
        leds[led + rows*60] = (255,100,0)
           
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

led = 29
while led>=360:
    for rows in range(6):
        leds[led + rows*60] = (0,0,0)

        time.sleep(.1)
        client.put_pixels(leds)
        led = led - 1 #or reverse if you want
led = 29
while led>=0:
    for rows in range(6):
        leds[led + rows*60] = (0,0,0)

        time.sleep(.1)
        client.put_pixels(leds)
        led = led - 1

led = 29
while led>=0:
 Run = True
 for rows in range(6):
        if led < 360:
          leds[led - rows*60] = (0,0,0)
        
 time.sleep(.1)
 client.put_pixels(leds)
 led = led + 1
 print (led)

         else:
           Run = False
           break 

for led in range(30): #pick out indeces: led = 0,1,2,3...
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)



    leds[59-led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)

    led = led + 1        


   # for rows in range(6):
   #     leds[28-led -rows*60]=(100,50,0)

  



