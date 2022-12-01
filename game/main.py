import pygame, sys
from settings import *
from debug import debug
from level import Level




class Game:
    def __init__(self):
        pygame.init()
        # Window sizes
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        # Window  title
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        self.level= Level()
        
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            
            self.level.run()
            
            debug(TITLE)
            
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()
    

# video: https://www.youtube.com/watch?v=QU1pPzEGrqw
# 28:16 (starting: creating the player)