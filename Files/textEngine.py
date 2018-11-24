import pygame
from glob import glob

class textGui():

    def __init__(self):
        if not pygame.font.get_init():
            pygame.font.init()
        self.extraFonts = []
        for font in glob('../Fonts/*.*'):
            self.extraFonts.append(pygame.font.Font(font, 50))

    def text(self, text, color=(255,255,255), antialias=True, useFont=None):
        tempText = pygame.font.Font.render(self.extraFonts[0], text, antialias, color)
        return tempText


