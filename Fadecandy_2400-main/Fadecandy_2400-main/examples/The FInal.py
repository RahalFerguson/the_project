import opc
import time
import pygame
from pygame import *
import random

leds = [(0, 0, 0)] * 360  # Black
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
fade_amount = 10


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
start_text, start_text_rect = writeText("animemation1", 100, 20, blue)  # 'name', height position, leter siza, color
#exit_text, exit_text_rect = writetext("End", 100, 20, red)

def menu():
    while True:
        Display.fill(white)
        Display.blit(title_text, title_text_rect)

        x, y = pygame.mouse.get_pos()

        Start = Display.blit(start_text, start_text_rect) # display word on pygame win
        animation_1 = Display.blit(start_text, start_text_rect)

        if Start.collidepoint((x, y)):
            if click:
                starting()
                print("Animation started")

        elif animation_1.collidepoint((x, y)):
            if click:
                animation_1()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True;

        pygame.display.update()


def stating():
    for led in range(30):  # pick out indeces:
        leds[led] = (44, 87, 132)  # bdazzled blue
        time.sleep(.09)
        client.put_pixels(leds)

        leds[59 - led] = (44, 87, 132)  # bdazzled blue
        time.sleep(.09)
        client.put_pixels(leds)

        led = led + 1

    led = 0

def abimation_1():
    while led < 30:  # scroll all rows at the same time
        for rows in range(1, 3):
            leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(1, 3):  # first three rows left to right
            leds[led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(3, 6):  # last three rows reversed (right to left)
            leds[59 - led + rows * 60] = (71, 0, 36)  # Triyan purple
        for rows in range(3, 6):
            leds[led + rows * 60] = (71, 0, 36)  # Triyan purple

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
        for led in range(29, len(leds)):
            for rows in range(6):
                if led < 96:
                    leds[led - rows * 60] = (0, 0, 0)

                    time.sleep(.1)
                    client.put_pixels(leds)
                    led = led + 1
                    print(led)

                else:
                    Run = False
                    break

    # first stick man
    # The Head
    leds[2] = (255, 255, 255)
    leds[3] = (255, 255, 255)
    leds[4] = (255, 255, 255)
    leds[62] = (255, 255, 255)
    leds[63] = (255, 255, 255)
    leds[64] = (255, 255, 255)

    # The body and arms
    leds[122] = (255, 255, 255)
    leds[123] = (255, 255, 255)
    leds[124] = (255, 255, 255)
    leds[181] = (255, 255, 255)
    leds[183] = (255, 255, 255)
    leds[185] = (255, 255, 255)
    leds[242] = (255, 255, 255)
    leds[243] = (255, 255, 255)
    leds[244] = (255, 255, 255)
    leds[301] = (255, 255, 255)
    leds[305] = (255, 255, 255)

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.5)

    leds = [(0, 0, 0)] * 360  # white

    # second stick man
    # The Head
    # leds[3] = (255, 255, 255)
    leds[3] = (255, 255, 255)
    leds[4] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63] = (255, 255, 255)
    leds[64] = (255, 255, 255)

    # The body and arms
    leds[122] = (255, 255, 255)
    leds[123] = (255, 255, 255)
    leds[124] = (255, 255, 255)
    leds[182] = (255, 255, 255)  # left hand
    leds[183] = (255, 255, 255)  # left hand
    leds[185] = (255, 255, 255)  # right hand
    leds[242] = (255, 255, 255)  # right Hand
    leds[243] = (255, 255, 255)  # left led
    leds[244] = (255, 255, 255)  # left leg
    leds[302] = (255, 255, 255)  # right led
    leds[305] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head
    # leds[3] = (255, 255, 255)
    leds[3] = (255, 255, 255)
    leds[4] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63] = (255, 255, 255)
    leds[64] = (255, 255, 255)

    # The body and arms
    leds[123] = (255, 255, 255)
    leds[124] = (255, 255, 255)
    leds[183] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185] = (255, 255, 255)  # right hand
    leds[243] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244] = (255, 255, 255)  # left leg
    leds[303] = (255, 255, 255)  # right led
    leds[305] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head
    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124] = (255, 255, 255)  # left hand
    leds[184] = (255, 255, 255)  # right hand
    leds[185] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244] = (255, 255, 255)  # left leg
    leds[304] = (255, 255, 255)  # right led
    leds[305] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head
    # leds[3] = (255, 255, 255)
    leds[5] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245] = (255, 255, 255)  # left led
    leds[305] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head
    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126] = (255, 255, 255)  # left hand
    leds[186] = (255, 255, 255)  # right hand
    leds[185] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246] = (255, 255, 255)  # left leg
    leds[306] = (255, 255, 255)  # right led
    leds[305] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head
    leds[6] = (255, 255, 255)
    leds[7] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66] = (255, 255, 255)
    leds[67] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126] = (255, 255, 255)
    leds[127] = (255, 255, 255)
    leds[185] = (255, 255, 255)
    leds[187] = (255, 255, 255)  # left hand
    leds[246] = (255, 255, 255)  # left hand
    leds[247] = (255, 255, 255)  # right hand
    leds[305] = (255, 255, 255)  # right Hand
    leds[307] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head
    leds[6] = (255, 255, 255)
    leds[7] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66] = (255, 255, 255)
    leds[67] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126] = (255, 255, 255)
    leds[127] = (255, 255, 255)
    leds[185] = (255, 255, 255)
    leds[187] = (255, 255, 255)  # left hand
    leds[246] = (255, 255, 255)  # left hand
    leds[247] = (255, 255, 255)  # right hand
    leds[305] = (255, 255, 255)  # right Hand
    leds[307] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head
    leds[6] = (255, 255, 255)
    leds[7] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66] = (255, 255, 255)
    leds[67] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126] = (255, 255, 255)
    leds[127] = (255, 255, 255)
    leds[128] = (255, 255, 255)
    leds[185] = (255, 255, 255)
    leds[187] = (255, 255, 255)  # left hand
    leds[246] = (255, 255, 255)  # left hand
    leds[247] = (255, 255, 255)  # right hand
    leds[305] = (255, 255, 255)  # right Hand
    leds[307] = (255, 255, 255)  # left leg
    leds[308] = (255, 255, 255)  # left leg
    leds[248] = (255, 255, 255)  # right leg
    leds[188] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head
    leds[6] = (255, 255, 255)
    leds[7] = (255, 255, 255)
    leds[8] = (255, 255, 255)
    leds[66] = (255, 255, 255)
    leds[67] = (255, 255, 255)
    leds[68] = (255, 255, 255)

    # The body and arms
    leds[126] = (255, 255, 255)
    leds[127] = (255, 255, 255)
    leds[128] = (255, 255, 255)
    leds[185] = (255, 255, 255)  # left hand
    leds[187] = (255, 255, 255)  # left hand
    leds[189] = (255, 255, 255)  # right hand
    leds[246] = (255, 255, 255)  # right Hand
    leds[247] = (255, 255, 255)  # left leg
    leds[248] = (255, 255, 255)  # left leg
    leds[305] = (255, 255, 255)  # right leg
    leds[309] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Tenth stick man
    # The Head
    # leds[6] = (255, 255, 255)
    leds[7] = (255, 255, 255)
    leds[8] = (255, 255, 255)
    # lds[66] = (255, 255, 255)
    leds[67] = (255, 255, 255)
    leds[68] = (255, 255, 255)

    # The body and arms
    leds[126] = (255, 255, 255)
    leds[127] = (255, 255, 255)
    leds[128] = (255, 255, 255)
    leds[185] = (255, 255, 255)  # left hand
    leds[187] = (255, 255, 255)  # left hand
    leds[189] = (255, 255, 255)  # right hand
    leds[246] = (255, 255, 255)  # right Hand
    leds[247] = (255, 255, 255)  # left leg
    leds[248] = (255, 255, 255)  # left leg
    leds[305] = (255, 255, 255)  # right leg
    leds[309] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Elevan stick man
    # The Head

    # leds[3] = (255, 255, 255)
    leds[7] = (255, 255, 255)
    leds[8] = (255, 255, 255)
    # leds[66] = (255, 255, 255)
    leds[67] = (255, 255, 255)
    leds[68] = (255, 255, 255)

    # The body and arms
    leds[126] = (255, 255, 255)
    leds[127] = (255, 255, 255)
    leds[128] = (255, 255, 255)
    leds[186] = (255, 255, 255)  # left hand
    leds[187] = (255, 255, 255)  # left hand
    leds[189] = (255, 255, 255)  # right hand
    leds[247] = (255, 255, 255)  # right Hand
    leds[246] = (255, 255, 255)  # left led
    leds[247] = (255, 255, 255)  # left leg
    leds[248] = (255, 255, 255)  # right led
    leds[306] = (255, 255, 255)  # right led`
    leds[309] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    x = 4
    # Twelth stick man
    # The Head
    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    x = 4

    # Thurteen stick man
    # The Head
    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fourteenth stick man
    # The Head

    x = 4

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # fiftwwnth stick man
    # The Head

    x = 4

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 8

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 8

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    x = 8

    # Fifth stick man
    # The Head
    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    x = 8

    # sixth stick man
    # The Head
    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    x = 8

    # seventh stick man
    # The Head
    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    x = 8

    # Eigth stick man
    # The Head
    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    x = 8

    # 8.1 stick man
    # The Head
    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 8

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 12

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 12

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 12

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 12

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 12

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 12

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 12

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 12

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 12

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 16

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 16

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 16

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 16

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 16

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 16

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 16

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 16

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 16

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 20

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 20

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 20

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 20

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 20

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 20

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 20

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 20

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 20

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 24

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 24

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 24

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 24

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 24

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 24

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 24

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 24

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 24

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 28

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 28

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 28

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 28

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 28

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 28

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 28

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 28

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 28

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 32

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 32

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 32

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 32

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 32

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 32

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 32

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 32

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 32

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 40

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 40
    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 40

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 40

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 40

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 40

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 40

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 40

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 40

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 44

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 44

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 44

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 44

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 44

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 44

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 44

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 44

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 44

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sisteenth stick man
    # The Head

    x = 48

    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[62] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[122 + x] = (255, 255, 255)
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[182 + x] = (255, 255, 255)  # left hand
    leds[183 + x] = (255, 255, 255)  # left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[242 + x] = (255, 255, 255)  # right Hand
    leds[243 + x] = (255, 255, 255)  # left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[302 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Third stick man
    # The Head

    x = 48
    # leds[3] = (255, 255, 255)
    leds[3 + x] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[63 + x] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    leds[123 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)
    leds[183 + x] = (255, 255, 255)
    # leds[123]=(255,255,255)#left hand
    # leds[183]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # right hand
    leds[243 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[303 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Forth stick man
    # The Head

    x = 48

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[4 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[64 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[184 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[244 + x] = (255, 255, 255)  # left leg
    leds[304 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Fifth stick man
    # The Head

    x = 48

    # leds[3] = (255, 255, 255)
    leds[5 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)
    # leds[65] =(255, 255, 255)

    # The body and arms
    leds[125 + x] = (255, 255, 255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[185 + x] = (255, 255, 255)  # left hand
    # leds[125]=(255,255,255)#right hand
    # leds[186]=(255,255,255)#right Hand
    leds[245 + x] = (255, 255, 255)  # left led
    leds[305 + x] = (255, 255, 255)  # left leg
    # leds[245]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # sixth stick man
    # The Head

    x = 48

    # leds[3] = (255, 255, 255)
    # leds[4] = (255, 255, 255)
    leds[6 + x] = (255, 255, 255)
    # leds[63] = (255, 255, 255)
    # leds[64] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)

    # The body and arms
    # leds[124]=(255,255,255)
    # leds[184]=(255,255,255)
    # leds[244]=(255,255,255)
    # leds[123]=(255,255,255)#left hand
    leds[126 + x] = (255, 255, 255)  # left hand
    leds[186 + x] = (255, 255, 255)  # right hand
    leds[185 + x] = (255, 255, 255)  # right Hand
    # leds[243]=(255,255,255)#left led
    leds[246 + x] = (255, 255, 255)  # left leg
    leds[306 + x] = (255, 255, 255)  # right led
    leds[305 + x] = (255, 255, 255)  # right led

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # seventh stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Eigth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    # leds[309]=(255,255,255)#left leg
    # leds[248]=(255,255,255)#right leg
    # leds[306]=(255,255,255)#right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # 8.1 stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    # leds[5] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    # leds[65] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[246 + x] = (255, 255, 255)  # left hand
    leds[247 + x] = (255, 255, 255)  # right hand
    leds[305 + x] = (255, 255, 255)  # right Hand
    leds[307 + x] = (255, 255, 255)  # left leg
    leds[308 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # right leg
    leds[188 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.1)

    leds = [(0, 0, 0)] * 360  # white

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.7)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 1

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[125 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 2

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 3

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[125 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 4

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 1

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 2

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 3

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 4

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 5

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 6

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[65 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 7

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[124 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

    # hand shake 1

    # Ningth stick man
    # The Head

    x = 48

    leds[6 + x] = (255, 255, 255)
    leds[7 + x] = (255, 255, 255)
    leds[8 + x] = (255, 255, 255)
    leds[66 + x] = (255, 255, 255)
    leds[67 + x] = (255, 255, 255)
    leds[68 + x] = (255, 255, 255)

    # The body and arms
    leds[126 + x] = (255, 255, 255)
    leds[127 + x] = (255, 255, 255)
    leds[128 + x] = (255, 255, 255)
    leds[185 + x] = (255, 255, 255)  # left hand
    leds[187 + x] = (255, 255, 255)  # left hand
    leds[189 + x] = (255, 255, 255)  # right hand
    leds[246 + x] = (255, 255, 255)  # right Hand
    leds[247 + x] = (255, 255, 255)  # left leg
    leds[248 + x] = (255, 255, 255)  # left leg
    leds[305 + x] = (255, 255, 255)  # right leg
    leds[309 + x] = (255, 255, 255)  # right leg

    client.put_pixels(leds)
    client.put_pixels(leds)

    time.sleep(.3)

    leds = [(0, 0, 0)] * 360  # white

menu()
