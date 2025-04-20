import pygame
from simulation import Simulation


pygame.init()

MySimulation = Simulation("particle_data.csv")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    MySimulation.update()