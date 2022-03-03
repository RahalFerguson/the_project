import opc
#from time import sleep
#import pygame
#from pygame import *
import random
import time
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PYgame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Color
#white = (255, 255, 255)
#black = (0, 0, 0)
#gray = (50, 50, 50)
#red = (255, 0, 0)
#green = (0, 255, 0)
#blue = (0, 0, 255)
#yellow = (255, 255, 0)

# Game Initialization
#pygame.init()

# Display Resolution
#width = 500
#height = 350
#surface = pygame.display.set_mode((width, height))


#def writeText(text, height_text, size, color):
#    font = pygame.font.SysFont("Arial", size, bold=True)  # Get font from pygame
#    text = font.render(text, 1, pygame.Color(color))  # draw text
#    text_rect = text.get_rect(center=(width // 2, height_text))  # this will be centered anyhow, but at y height
#    return text, text_rect


#title_text, title_text_rect = writeText("Python Project", 20, 50, black)
#START_text, START_text_rect = writeText("START", 100, 20, blue)
#animation_1_text, animation_1_text_rect = writeText("Animation 1", 130, 20,
#                                                    blue)  # 'name', height position, leter siza, color
#exit_text, exit_text_rect = writeText("End", 150, 20, red)

#def menu():
#    while True:
#        surface.fill(white)
#        surface.blit(title_text, title_text_rect)

#        x, y = pygame.mouse.get_pos()

#        Start = surface.blit(START_text, START_text_rect)  # display word on pygame win
#        Animation_1 = surface.blit(animation_1_text, animation_1_text_rect)
#        End = surface.blit(exit_text, exit_text_rect)

#        if Start.collidepoint((x, y)):
#            if click:
#                START()
#                print("Animation started")

#        elif Animation_1.collidepoint((x, y)):
#            if click:
#                Animation_1()

#        elif End.collidepoint((x, y)):
#            if click:
#                end_Animation()

#        click = False
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                pygame.quit()
#                return
#            elif event.type == MOUSEBUTTONDOWN:
#                if event.button == 1:
#                    click = True;

#        pygame.display.update()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

leds = [(0, 0, 0)] * 360  # Black
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
fade_amount = 10

#def START():

for led in range(30):  # pick out indeces:
    leds[led] = (44, 87, 132)  # bdazzled blue
    time.sleep(.09)
    client.put_pixels(leds)

    leds[59 - led] = (44, 87, 132)  # bdazzled blue
    time.sleep(.09)
    client.put_pixels(leds)

    led = led + 1

led = 0

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

leds[3] = (255, 255, 255)
leds[4] = (255, 255, 255)

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

          #H

leds[1] = (131, 182, 146)
leds[61] = (131, 182, 146)
leds[121] = (131, 182, 146)
leds[181] = (131, 182, 146)
leds[241] = (131, 182, 146)
leds[301] = (131, 182, 146)

leds[0] = (131, 182, 146)
leds[60] = (131, 182, 146)
leds[120] = (131, 182, 146)
leds[180] = (131, 182, 146)
leds[240] = (131, 182, 146)
leds[300] = (131, 182, 146)

leds[123] = (131, 182, 146)
leds[124] = (131, 182, 146)
leds[184] = (131, 182, 146)
leds[183] = (131, 182, 146)

leds[182] = (131, 182, 146)
leds[185] = (131, 182, 146)
leds[122] = (131, 182, 146)
leds[125] = (131, 182, 146)

leds[6] = (131, 182, 146)
leds[66] = (131, 182, 146)
leds[126] = (131, 182, 146)
leds[186] = (131, 182, 146)
leds[246] = (131, 182, 146)
leds[306] = (131, 182, 146)

leds[5] = (131, 182, 146)
leds[65] = (131, 182, 146)
leds[125] = (131, 182, 146)
leds[185] = (131, 182, 146)
leds[245] = (131, 182, 146)
leds[305] = (131, 182, 146)

         #E
leds[8] = (249, 173, 160)
leds[68] = (249, 173, 160)
leds[128] = (249, 173, 160)
leds[188] = (249, 173, 160)
leds[248] = (249, 173, 160)
leds[308] = (249, 173, 160)

leds[9] = (249, 173, 160)
leds[69] = (249, 173, 160)
leds[129] = (249, 173, 160)
leds[189] = (249, 173, 160)
leds[249] = (249, 173, 160)
leds[309] = (249, 173, 160)

leds[10] = (249, 173, 160)
leds[11] = (249, 173, 160)
leds[70] = (249, 173, 160)
leds[130] = (249, 173, 160)
leds[131] = (249, 173, 160)
leds[190] = (249, 173, 160)
leds[191] = (249, 173, 160)
leds[12] = (249, 173, 160)
leds[132] = (249, 173, 160)
leds[192] = (249, 173, 160)
leds[250] = (249, 173, 160)
leds[310] = (249, 173, 160)
leds[311] = (249, 173, 160)
leds[312] = (249, 173, 160)

           #l
leds[14] = (249, 98, 125)
leds[74] = (249, 98, 125)
leds[134] = (249, 98, 125)
leds[194] = (249, 98, 125)
leds[254] = (249, 98, 125)
leds[314] = (249, 98, 125)

leds[15] = (249, 98, 125)
leds[75] = (249, 98, 125)
leds[135] = (249, 98, 125)
leds[195] = (249, 98, 125)
leds[255] = (249, 98, 125)
leds[315] = (249, 98, 125)

leds[256] = (249, 98, 125)
leds[316] = (249, 98, 125)


leds[257] = (249, 98, 125)
leds[317] = (249, 98, 125)
leds[258] = (249, 98, 125)
leds[318] = (249, 98, 125)

          #l
leds[20] = (249, 98, 125)
leds[80] = (249, 98, 125)
leds[140] = (249, 98, 125)
leds[200] = (249, 98, 125)
leds[260] = (249, 98, 125)
leds[320] = (249, 98, 125)

leds[21] = (249, 98, 125)
leds[81] = (249, 98, 125)
leds[141] = (249, 98, 125)
leds[201] = (249, 98, 125)
leds[261] = (249, 98, 125)
leds[321] = (249, 98, 125)

leds[262] = (249, 98, 125)
leds[322] = (249, 98, 125)


leds[263] = (249, 98, 125)
leds[323] = (249, 98, 125)
leds[264] = (249, 98, 125)
leds[324] = (249, 98, 125)

          #o
leds[26] = (198, 91, 124)
leds[86] = (198, 91, 124)
leds[146] = (198, 91, 124)
leds[206] = (198, 91, 124)
leds[266] = (198, 91, 124)
leds[326] = (198, 91, 124)

leds[27] = (198, 91, 124)
leds[87] = (198, 91, 124)
leds[147] = (198, 91, 124)
leds[207] = (198, 91, 124)
leds[267] = (198, 91, 124)
leds[327] = (198, 91, 124)

leds[28] = (198, 91, 124)
leds[88] = (198, 91, 124)
leds[268] = (198, 91, 124)
leds[328] = (198, 91, 124)

leds[29] = (198, 91, 124)
leds[89] = (198, 91, 124)
leds[269] = (198, 91, 124)
leds[329] = (198, 91, 124)

leds[30] = (198, 91, 124)
leds[90] = (198, 91, 124)
leds[150] = (198, 91, 124)
leds[210] = (198, 91, 124)
leds[270] = (198, 91, 124)
leds[330] = (198, 91, 124)

leds[31] = (198, 91, 124)
leds[91] = (198, 91, 124)
leds[151] = (198, 91, 124)
leds[211] = (198, 91, 124)
leds[271] = (198, 91, 124)
leds[331] = (198, 91, 124)

              #Smile face
    #Eye
leds[94] = (91, 55, 88)
leds[154] = (91, 55, 88)

leds[95] = (91, 55, 88)
leds[155] = (91, 55, 88)

leds[99] = (91, 55, 88)
leds[159] = (91, 55, 88)

leds[100] = (91, 55, 88)
leds[160] = (91, 55, 88)

              #smile
leds[275] = (91, 55, 88)
leds[276] = (91, 55, 88)
leds[277] = (91, 55, 88)
leds[278] = (91, 55, 88)

leds[279] = (91, 55, 88)

client.put_pixels(leds)
client.put_pixels(leds)

time.sleep(1)

led = 0

while led < 60:  # scroll all rows at the same time
    for rows in range(6):
        leds[59 - led + rows * 60] = (0, 0, 0)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

led = 29
Run = True
while Run:
    for rows in range(6):
        if led < 59:
         leds[ led + rows * 60] = (255, 0, 0)

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
        if led < 59:
         leds[ 59 - led + rows * 60] = (255, 0, 0)

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

led = 29
Run = True
while Run:
    for rows in range(6):
        if led < 60:
         leds[59 - led - rows * 60] = (255, 0, 0)

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
        if led < 59:
         leds[59 - led + rows * 60] = (255, 0, 0)

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

led = 30
Run = True
while Run:
    for rows in range(6):
        if led < 60:
         leds[59 - led - rows * 60] = (255, 0, 0)

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
        if led < 59:
         leds[59 - led + rows * 60] = (255, 0, 0)

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

led = 31
Run = True
while Run:
    for rows in range(6):
        if led < 60:
         leds[59 - led - rows * 60] = (255, 0, 0)

         time.sleep(.15)
         client.put_pixels(leds)
         led = led + 1

         print(led)

        else:
         Run= False
         break

led = 32

while led < 60:  # scroll all rows at the same time
    for rows in range(1):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(1):
        leds[59 - led + rows * 60] = (255, 255, 255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6


    client.put_pixels(leds)
    time.sleep(.1)


led = 33

while led < 60:  # scroll all rows at the same time
    for rows in range(2):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(2):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 34

while led < 60:  # scroll all rows at the same time
    for rows in range(1):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(1):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 36

while led < 60:  # scroll all rows at the same time
    for rows in range (2, 3):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range (2, 3):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 35

while led < 60:  # scroll all rows at the same time
    for rows in range(3, 4):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(3, 4):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 36

while led < 60:  # scroll all rows at the same time
    for rows in range(3, 4):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(3, 4):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 37

while led < 60:  # scroll all rows at the same time
    for rows in range(3, 4):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(3, 4):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 36

while led < 60:  # scroll all rows at the same time
    for rows in range(4, 5):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(4, 5):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 33

while led < 60:  # scroll all rows at the same time
    for rows in range(5, 6):
        leds[led + rows * 60] = (255, 255, 255)
    for rows in range(5, 6):
        leds[59 - led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 6

    client.put_pixels(leds)
    time.sleep(.1)

led = 0
while led >= 360:
    for rows in range(6):
        leds[led + rows * 60] = (255, 255, 255)
        for rows in range(6):
            leds[59 - led + rows * 60] = (255, 255, 255)

        time.sleep(.1)
        client.put_pixels(leds)
        led = led + 1

led = 30

while led < 60:  # scroll all rows at the same time
    for rows in range(6):
        leds[59 - led + rows * 60] = (255, 255, 255)
    for rows in range(6):
        leds[led + rows * 60] = (255, 255, 255)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

#menu()



