import pygame,sys,random

class ParticleStar:

    def __init__(self):
        self.particles = []
        self.star = pygame.image.load('Star.png').convert_alpha()
        self.width = self.star.get_width()
        self.height = self.star.get_height()


    def emit(self):

        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x+= particle[1]
                particle[0].y += particle[2]
                particle[3] -= 0.2

                screen.blit(self.star,particle[0])





    def add_particles(self):
        if pygame.mouse.get_focused():
            pos_x,pos_y = pygame.mouse.get_pos()
            pos_x -= self.width//2
            pos_y -= self.height//2

            direction_x = random.randint(-3,3)
            direction_y = random.randint(-3,3)
            lifetime = random.randint(4,10)
            particle_rect = pygame.Rect(pos_x,pos_y,self.width,self.height)

            self.particles.append([particle_rect,direction_x,direction_y,lifetime])

    def delete_particles(self):
        # delete particles after a certain time
        particles_copy = [particle for particle in self.particles if particle[3] > 0]
        self.particles = particles_copy
class ParticleNyan:

    def __init__(self):
        self.particles = []
        self.size = 12


    def emit(self):

        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x -= 1
                pygame.draw.rect(screen,particle[1],particle[0])


        
        self.draw_nyancat()


    def add_particles(self,offset,color):
        pos_x,pos_y = pygame.mouse.get_pos()
        pos_y += offset

        particle_rect = pygame.Rect(pos_x - self.size//2,pos_y - self.size//2,self.size,self.size)


        self.particles.append((particle_rect,color))

    def delete_particles(self):
        # delete particles after a certain time
        particles_copy = [particle for particle in self.particles if particle[0].x > 0]
        self.particles = particles_copy
    
    def draw_nyancat(self):
        nyan_rect = nyan_cat.get_rect(center=pygame.mouse.get_pos())
        screen.blit(nyan_cat,nyan_rect)
class ParticleList:

    def __init__(self):
        self.particles = []


    def emit(self):

        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][0] += particle[-1][0]
                particle[0][1] += particle[-1][1]
                particle[1] -= 0.2

                pygame.draw.circle(screen,WHITE,particle[0],int(particle[1]))





    def add_particles(self):
        if pygame.mouse.get_focused():
            pos_x,pos_y = pygame.mouse.get_pos()
            radius = 10

            direction_x = random.randint(-3,3)
            direction_y = random.randint(-3,3)
            particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]

            self.particles.append(particle_circle)

    def delete_particles(self):
        # delete particles after a certain time
        particles_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particles_copy



pygame.init()


SCREEN_WIDTH = SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
nyan_cat = pygame.image.load('nyan_cat.png').convert_alpha()

star = pygame.image.load('star.png').convert_alpha()
clock = pygame.time.Clock()
FPS = 120
BGCOLOR = (30,30,30)
WHITE = (255,255,255)


particle1 = ParticleList()
particle2 = ParticleNyan()
particle3 = ParticleStar()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            #particle1.add_particles()
            #particle2.add_particles(-30,pygame.Color("Red"))
            #particle2.add_particles(-18,pygame.Color("Orange"))
            #particle2.add_particles(-6,pygame.Color("Yellow"))
            #particle2.add_particles(6,pygame.Color("Green"))
            #particle2.add_particles(18,pygame.Color("Blue"))
            #particle2.add_particles(30,pygame.Color("Purple"))
            particle3.add_particles()



    screen.fill(BGCOLOR)
    #particle1.emit()
    #particle2.emit()
    particle3.emit()
    pygame.display.update()
    clock.tick(60)



