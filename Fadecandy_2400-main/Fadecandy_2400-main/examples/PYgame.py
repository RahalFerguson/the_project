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