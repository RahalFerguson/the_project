import opc
import time
import random
import pygame
from pygame import *

# Color
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Initialization
pygame.init()

# Display Resolution
width = 500
height = 350
Display = pygame.display.set_mode((width, height))


def writeText(text, height_text, size, color):
    font = pygame.font.SysFont("Arial", size, bold=True)  # Get font from pygame
    text = font.render(text, 1, pygame.Color(color))  # draw text
    text_rect = text.get_rect(center=(width // 2, height_text))  # this will be centered anyhow, but at y height
    return text, text_rect


title_text, title_text_rect = writeText("Python Project", 20, 50, black)
start_text, start_text_rect = writeText("START", 100, 20, blue)
#exit_text, exit_text_rect = writetext("End", 100, 20, red)

def menu():
    while True:
        Display.fill(white)
        Display.blit(title_text, title_text_rect)

        x, y = pygame.mouse.get_pos()

        Start = Display.blit(start_text, start_text_rect)

        if Start.collidepoint((x, y)):
            if click:
                # Call your functions here
                print("Animation started")

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True;

        pygame.display.update()


menu()

leds = [(0, 0, 0)] * 360  # black
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
fade_amount = 10


# for led in leds: # pick out an element: led = (255,255,255)
for led in range(30):  # pick out indeces: led = 0,1,2,3...
    leds[led] = (44, 87, 132) #bdazzled blue
    time.sleep(.09)
    client.put_pixels(leds)

    leds[59 - led] = (44, 87, 132) #bdazzled blue
    time.sleep(.09)
    client.put_pixels(leds)

    led = led + 1  # or reverse if you want
# led = 59
# while led>=0:

#    leds[led] = (0,255,0)
#    time.sleep(.1)
#    client.put_pixels(leds)
#    led = led - 1 #or reverse if you want

led = 0
while led < 30:  # scroll all rows at the same time
    for rows in range(1, 3):
        leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
    # leds[led+  0] = (0,0,255) #row 1 - 0-60
    # leds[led+ 60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
    # leds[led+120] = (0,0,255)
    # leds[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
    # leds[led+240] = (0,0,255)
    # leds[led+300] = (0,0,255)
    for rows in range(1, 3):  # first three rows left to right
        leds[led + rows * 60] = (91, 24, 101)  # midnight
    for rows in range(3, 6):  # last three rows reversed (right to left)
        leds[59 - led + rows * 60] = (71, 0, 36) #Triyan purple
    for rows in range(3, 6):
        leds[led + rows * 60] = (71, 0, 36) #Triyan purple

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

led = 59
while led >= 360:
    for rows in range(6):
        leds[led + rows * 60] = (0, 0, 0)

        time.sleep(.1)
        client.put_pixels(leds)
        led = led - 1  # or reverse if you want

led = 29
while led >= 0:
    for rows in range(6):
        leds[led + rows * 60] = (0, 0, 0)

        time.sleep(.15)
        client.put_pixels(leds)
        led = led - 1

led = 59
while led >= 0:
    for rows in range(6):
        leds[led + rows * 60] = (0, 0, 0)

        time.sleep(.15)
        client.put_pixels(leds)
        led = led - 1

led = 59

Run = True
while Run:
    #for led in range(0, len(leds)):
        for rows in range(6):
            if led < 65:
                leds[led - rows * 60] = (0, 0, 0)

                time.sleep(.1)
                client.put_pixels(leds)
                led = led + 1
                print(led)

            else:
                Run = False
                break

led = 29
while led >= 0:
    for rows in range(6):
        leds[led + rows * 60] = (0, 0, 0)

        time.sleep(.15)
        client.put_pixels(leds)
        led = led + 1