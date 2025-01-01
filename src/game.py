import sys
import pygame
from ball import Ball
from messi import Messi


class Game:
    def __init__(self):
        self.name = "Żonglerka"
        self.width = 900
        self.height = 700
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        self.clock = pygame.time.Clock()
        self.running = True
        self.boisko = pygame.image.load("../graphs/boisko.png").convert_alpha()

        #Game
        self.player = Messi(322,350)
        self.ball = Ball(440, 550)

        #Music
        pygame.mixer.music.load("../music/K'NAAN - Wavin' Flag (Coca-Cola Celebration Mix).mp3")  # Ścieżka do pliku muzycznego

        # Rozpoczęcie odtwarzania od 30. sekundy
        pygame.mixer.music.play(-1, start=7)

    def update(self):
        self.ball.update()
        self.player.update(self.ball)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.player.flag:
                        self.player.kick()


        if self.ball.rect.bottom > 630:
            self.ball.reset()
            self.player.reset()


    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.boisko, (0, 0))
        self.player.draw_player(self.screen)
        self.ball.draw_ball(self.screen)

        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.update()
            self.clock.tick(60)

    def game_over(self):
        pass
