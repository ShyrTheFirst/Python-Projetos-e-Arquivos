import pygame, os, random, sys

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 650

os.environ['SDL_VIDEO_WINDOW_POS']= '%d,%d' %(150,50)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Water Drop using Pygame')

FPS = 60

clock = pygame.time.Clock()

class WaterParticle:
    alpha_layer_qty = 2
    alpha_glow_difference_constant = 1.7

    def __init__(self, x=SCREEN_WIDTH //2, y=SCREEN_HEIGHT//2, r=5):
        self.x, self.y = pygame.mouse.get_pos()
        self.r = r
        self.original_r = r
        self.alpha_layers = WaterParticle.alpha_layer_qty
        self.alpha_glow = WaterParticle.alpha_glow_difference_constant
        max_surf_size = 2*self.r*self.alpha_layers*self.alpha_layers*self.alpha_glow
        self.surf = pygame.Surface((max_surf_size, max_surf_size), pygame.SRCALPHA)
        self.burn_rate = 0.1*random.randint(1,10)

    def update(self):
        self.y += 7 + self.r
        self.x -= random.randint(1, 1)
        self.original_r -= self.burn_rate
        self.r = int(self.original_r)
        self.r = int(self.original_r)
        if self.r <= 0:
            self.r = 1

    def draw(self):
        
        max_surf_size = 2*self.r*self.alpha_layers*self.alpha_layers*self.alpha_glow
        self.surf = pygame.Surface((max_surf_size,max_surf_size), pygame.SRCALPHA)
        for i in range(self.alpha_layers, -1,-1):
            alpha = 180  - i * (255//self.alpha_layers -5)
            if alpha <= 0:
                alpha = 0
            radius = self.r*i*i*self.alpha_glow
            if self.r == 4 or self.r ==3:
                r, g, b = (255,0,150)
            elif self.r == 2:
                r, g, b = (255,150,150)
            else:
                r, g, b = (10,10,150)
            r,g,b = (10,0,210)
            color = (r,g,b,alpha)
            pygame.draw.circle(self.surf,color,(self.surf.get_width()//2, self.surf.get_height()//2), radius)
        screen.blit(self.surf, self.surf.get_rect(center=(self.x,self.y)))

class Water:
    def __init__(self, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2):
        self.x = x
        self.y = y
        self.water_intensity = 25
        self.water_particles = []
        for i in range(self.water_intensity*25):
            self.water_particles.append(WaterParticle(self.x+random.randint(-5,5), self.y, random.randint(1,5)))

    def draw_water(self):
        for i in self.water_particles:
            if i.original_r <= 0:
                self.water_particles.remove(i)
                self.water_particles.append(WaterParticle(self.x+random.randint(-5,5),self.y, random.randint(1,5)))
                del i
                continue
            i.update()
            i.draw()

water = Water()

def check_events(events):
    for e in events:
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def main_window():
    while True:
        events = pygame.event.get()
        check_events(events)
        screen.fill((0,0,0))
        water.draw_water()
        pygame.display.update()
        clock.tick(FPS)

main_window()
