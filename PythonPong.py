# Python Pong

import pygame

# variables

WIDTH = 750
HEIGHT = 600
BORDER = 10
VELOCITY = 1
FRAMERATE = 250

fgColour = pygame.Color("white")
bgColour = pygame.Color("black")
ballColour = pygame.Color("white")


# classes

class Ball:

    RADIUS = 10
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        pygame.draw.circle(screen, colour, (self.x, self.y), self.RADIUS)

    def update(self):
        global bgColour, fgColour
        self.show(bgColour)
        
        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER+self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER+self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy

        elif newx > WIDTH-BORDER and (ptopy <= newy and newy <= pbottomy):
            self.vx = -self.vx
        
        else:
            self.show(bgColour)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgColour)

class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, colour):
        pygame.draw.rect(screen, colour,
                         pygame.Rect(WIDTH-self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))

    def update(self):
        global bgColour, fgColour
        global ptopy, pbottomy
        
        newy = pygame.mouse.get_pos()[1]
        ptopy = newy-50
        pbottomy = newy+50

        if newy-self.HEIGHT//2 > BORDER:
            self.show(bgColour)
            self.y = newy
            self.show(fgColour)

# create objects

ballPlay = Ball(WIDTH-Ball.RADIUS, (HEIGHT//2), -VELOCITY, -VELOCITY)
paddle = Paddle(HEIGHT//2)

# screen

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(bgColour)

pygame.draw.rect(screen, fgColour, pygame.Rect((0,0), (WIDTH, BORDER)))
pygame.draw.rect(screen, fgColour, pygame.Rect(0,0, BORDER, HEIGHT))
pygame.draw.rect(screen, fgColour, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))

ballPlay.show(ballColour)
paddle.show(fgColour)

# quit when x is clicked
# note: this doesn't work in all OS

clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)

    ballPlay.update()
    paddle.update()
    
    pygame.display.flip()

pygame.quit()




