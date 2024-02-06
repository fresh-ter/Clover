import sys
import pygame
from Pelcod.pelcod import PelcoD

pygame.joystick.init()
pygame.init()
clock = pygame.time.Clock()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

p = PelcoD(port=sys.argv[1], baudrate=9600)

x = 0
y = 0
z = 0

pan_speed = '\x20'
tilt_speed = '\x20'

p.setPanSpeed(0x10)
p.setTiltSpeed(0x10)

try:
    while True:
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >= 1:
                        x = 1
                    elif event.value <= -1:
                        x = -1
                    else:
                        x = 0
                elif event.axis == 1:
                    if event.value >= 1:
                        y = 1
                    elif event.value <= -1:
                        y = -1
                    else:
                        y = 0
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    z = 1
                elif event.button == 2:
                    z = -1
                elif event.button == 5:
                    p.setPanSpeed(0x20)
                    p.setTiltSpeed(0x20)
                elif event.button == 4:
                    p.setPanSpeed(0x00)
                    p.setTiltSpeed(0x00)
                elif event.button == 9:
                    p.home()
                    continue
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 0 or event.button == 2:
                    z = 0
                elif event.button == 5 or event.button == 4:
                    p.setPanSpeed(0x10)
                    p.setTiltSpeed(0x10)

            print(x, y, p.getPanSpeed(), p.getTiltSpeed())

            p.move(x, y, z)
            
            print()
            print()


        clock.tick(60)
except KeyboardInterrupt:
    p.unconnect()
    print("Unconnected")
