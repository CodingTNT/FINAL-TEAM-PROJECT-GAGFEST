import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deal with it!")

COLORS = ["#6622CC", "#A755C2", "#B07C9E", "#B59194", "#D2A1B8"]
COLORS = [pygame.Color(c) for c in COLORS]
FONT = pygame.font.Font(None, 36)

SOUNDS = {
    "G": pygame.mixer.Sound("439012__fourthwoods__kara-g.ogg"), 
    "I": pygame.mixer.Sound("439066__fourthwoods__lexie-i-2.ogg"),
    "O": pygame.mixer.Sound("439059__fourthwoods__lexie-o-4.ogg"),
}

# 定义粒子类
class Particle:
    def __init__(self, x, y, text, color):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.lifespan = random.randint(40, 100)
        self.velocity = [random.uniform(-3, 3), random.uniform(-3, 3)]  

    def update(self):

        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.lifespan -= 1

    def draw(self, surface):

        if self.lifespan > 0:
            text_surface = FONT.render(self.text, True, self.color)
            surface.blit(text_surface, (self.x, self.y))


particles = []


clock = pygame.time.Clock()
running = True

while running:
    screen.fill((250, 250, 250))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_particle = Particle(
        x=mouse_x,
        y=mouse_y,
        text=random.choice(["G", "I", "O"]),
        color=random.choice(COLORS),
    )
    particles.append(new_particle)

    if new_particle.text in SOUNDS:
        SOUNDS[new_particle.text].play()


    for particle in particles[:]:
        particle.update()
        if particle.lifespan <= 0:
            particles.remove(particle)
        else:
            particle.draw(screen)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
sys.exit()
