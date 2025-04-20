import pygame
import pandas
import math
import time
import copy
G = 1000
TIME_FRAME = 0.01

class Simulation:
    class Particle:
        def __init__(self,mass,xcor,ycor,xspeed,yspeed):
            self.mass = mass
            self.xcor = xcor
            self.ycor = ycor
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.xaccel = 0
            self.yaccel = 0
        def add_gravity(self,Particle):
            rx =Particle.xcor - self.xcor
            ry =Particle.ycor - self.ycor
            d = math.sqrt(rx*rx+ry*ry)
            if d > 10:
                self.xaccel+= (G*Particle.mass*rx)/(d*d*d)
                self.yaccel+= (G*Particle.mass*ry)/(d*d*d)
        def reset_gravity(self):
            self.xaccel = 0
            self.yaccel = 0
        def move(self):
            self.xcor+=self.xspeed*TIME_FRAME + (self.xaccel*TIME_FRAME*TIME_FRAME)/2
            self.ycor+=self.yspeed*TIME_FRAME + (self.yaccel*TIME_FRAME*TIME_FRAME)/2
            self.xspeed+=self.xaccel*TIME_FRAME
            self.yspeed+=self.yaccel*TIME_FRAME
            self.reset_gravity()
        


            

            

    def __init__(self,dataframe_adress):
        self.particle_list = []
        particle_data = pandas.read_csv(dataframe_adress)
        maxcord = 0
        for i,row in particle_data.iterrows():
            maxcord = max(abs(row.xcor),abs(row.ycor),maxcord)
            self.particle_list.append(self.Particle(row.mass,row.xcor,row.ycor,row.xspeed,row.yspeed))
        self.screen = pygame.display.set_mode((int(2*maxcord+200),int(2*maxcord+200)))
        pygame.display.set_caption(f"Simulation N = {len(particle_data)}")
        self.draw()

    def draw(self):
        self.screen.fill((0,0,0))
        width, height = self.screen.get_size()
        for particle in self.particle_list:
            x = width/2 + particle.xcor
            y = height/2 - particle.ycor
            pygame.draw.circle(self.screen,"white",(x,y),5)
        pygame.display.update()

    def update(self):
        particle_copy = copy.deepcopy(self.particle_list)

        for pcopy in particle_copy:
            for p in self.particle_list:
                pcopy.add_gravity(p)
            pcopy.move()
        self.particle_list = particle_copy
        self.draw()
        time.sleep(TIME_FRAME)
        

        
            
    
    

