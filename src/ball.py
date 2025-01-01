import pygame

class Ball:
    def __init__(self,x,y):
        self.image = pygame.transform.scale(pygame.image.load("../graphs/pilka.png").convert_alpha(), (50,50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_frect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.speedx = 0
        self.speedy = 0
        self.direction = pygame.math.Vector2(0,0)
        self.flag = False


    def draw_ball(self, screen):
        #pygame.draw.rect(screen, "black", self.rect)
        screen.blit(self.image, self.rect)


    def move_ball(self):
        if self.flag:
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            self.speedy += 0.7


    def jump(self, rect):
        self.flag = True
        self.direction = (self.get_center(self.rect) - self.get_center(rect)).normalize()
        self.speedx = self.direction.x*5
        self.speedy = -25

    def bounce(self):
        if self.rect.left < -5:
            self.speedx *= -1
        if self.rect.right > 905:
            self.speedx *= -1



    def get_center(self, rect):
        return pygame.math.Vector2(rect.x + rect.width / 2, rect.y + rect.height / 2)


    def update(self):
        self.move_ball()
        self.bounce()


    def reset(self):
        self.rect.center = (self.x, self.y)
        self.flag = False
