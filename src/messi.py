import pygame

class Messi:
    def __init__(self,x,y):
        self.spriteSheet = pygame.transform.scale2x(pygame.image.load("../graphs/messi2.png").convert_alpha())
        self.spriteSheet.set_colorkey((255, 255, 255))
        self.frameSize = 256
        self.frames = [self.getFrame(x, 0) for x in range(6)]
        self.rotated_frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
        self.framesRight = [self.frames[4], self.frames[3], self.frames[5], self.frames[3]]
        self.framesLeft = [self.rotated_frames[4], self.rotated_frames[3], self.rotated_frames[5], self.rotated_frames[3]]
        self.rightKick = [self.frames[0], self.frames[1], self.frames[2], self.frames[1], self.frames[0], self.frames[3]]
        self.leftKick = [self.rotated_frames[0], self.rotated_frames[1], self.rotated_frames[2], self.rotated_frames[1], self.rotated_frames[0],self.rotated_frames[3]]

        self.currentFrames = [self.frames[3]]
        self.flag = False

        self.resetx = x
        self.resety = y

        self.x = x
        self.y = y
        self.speed = 4
        self.flag = False
        self.current_frame = 0

        self.currentFrame = self.frames[3]

        self.kapeczki = 0
        self.font = pygame.font.Font("../fonts/PixelifySans-Regular.ttf", 40)

    def getFrame(self, frame_x, frame_y):
        rect = pygame.Rect(frame_x * self.frameSize, frame_y * self.frameSize, self.frameSize, self.frameSize)
        frame = self.spriteSheet.subsurface(rect)
        return frame


    def draw_player(self, screen):
        text = self.font.render(f"Kapeczki: {self.kapeczki}", True, "white")  # Tworzenie napisu
        screen.blit(text, (10,10))
        speed = 6
        self.current_frame = self.current_frame + 1
        if self.current_frame >= speed*len(self.currentFrames):
            self.current_frame = 0

        self.currentFrame = self.currentFrames[self.current_frame // speed]
        screen.blit(self.currentFrame, (self.x, self.y))
        if (self.currentFrames == self.rightKick or self.currentFrames == self.leftKick) and self.current_frame // speed == 5:
            self.flag = False


    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not self.flag:
                self.currentFrames = self.framesLeft
            self.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            if not self.flag:
                self.currentFrames = self.framesRight
        else:
            if not self.flag:
                if self.currentFrames == self.framesRight or self.currentFrames == [self.frames[3]] or self.currentFrames == self.rightKick:
                    self.currentFrames = [self.frames[3]]
                else:
                    self.currentFrames = [self.rotated_frames[3]]


    def kick(self):
        if self.currentFrames == self.framesRight or self.currentFrames == [self.frames[3]]:
            self.flag = True
            self.currentFrames = self.rightKick
        if self.currentFrames == self.framesLeft or self.currentFrames == [self.rotated_frames[3]]:
            self.flag = True
            self.currentFrames = self.leftKick
        self.current_frame = 0


    def collide(self, ball):

        if self.currentFrame == self.rightKick[0]:
            rect = pygame.FRect(self.x+160, self.y+230, 24, 24)
            if rect.colliderect(ball.rect):
                ball.jump(rect)
                self.kapeczki += 1

        elif self.currentFrame == self.rightKick[1]:
            rect = pygame.FRect(self.x+174, self.y+210, 24, 24)
            if rect.colliderect(ball.rect):
                ball.jump(rect)
                self.kapeczki += 1

        elif self.currentFrame == self.rightKick[2]:
            rect = pygame.FRect(self.x+184, self.y+172, 24, 24)
            if rect.colliderect(ball.rect):
                ball.jump(rect)
                self.kapeczki += 1

        elif self.currentFrame == self.leftKick[0]:
            rect = pygame.FRect(self.x+256-160, self.y+230, 24, 24)
            if rect.colliderect(ball.rect):
                ball.jump(rect)
                self.kapeczki += 1

        elif self.currentFrame == self.leftKick[1]:
            rect = pygame.FRect(self.x+256-174, self.y+210, 24, 24)
            if rect.colliderect(ball.rect):
                ball.jump(rect)
                self.kapeczki += 1

        elif self.currentFrame == self.leftKick[2]:
            rect = pygame.FRect(self.x+256-184, self.y+172, 24, 24)
            if rect.colliderect(ball.rect):
                ball.jump(rect)
                self.kapeczki += 1


    def update(self, ball):
        self.collide(ball)
        self.move_player()

    def reset(self):
        self.x = self.resetx
        self.y = self.resety
        self.kapeczki = 0
        self.flag = False
