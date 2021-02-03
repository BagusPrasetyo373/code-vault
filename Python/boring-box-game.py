import pygame
from pygame.locals import *

pygame.init()

class Window:
  def __init__(self,obj,width,height):
    self.obj = obj
    self.width = width
    self.height = height
 
class Player:
  def __init__(self,obj,x,y,w,h):
    self.obj = obj
    self.x = x
    self.y = y
    self.w = w
    self.h = h
 
class Mainloop:
  def __init__(self,loop):
    self.loop = loop
  def mainloop():
    while Mainloop.loop:
        for event in pygame.event.get():
        	if event.type == QUIT: Mainloop.loop = False
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
          	Player.y -= 1
          	if(not (Player.y % Window.height)): Player.y += 1
        elif keys[K_DOWN]:
          	Player.y += 1
          	if(not ((Player.y + Player.h) % Window.height)): Player.y -= 1
        elif keys[K_LEFT]:
          	Player.x -= 1
          	if(not (Player.x % Window.width)): Player.x += 1
        elif keys[K_RIGHT]:
        	Player.x += 1
        	if(not ((Player.x + Player.w) % Window.width)): Player.x -= 1
        Window.obj.fill((0,0,0))
        pygame.draw.rect(Window.obj, (255,255,255), (Player.x,Player.y,Player.w,Player.h))
        pygame.display.update()

pygame.display.set_caption("Boring box game")

Window.width = 500
Window.height = 450
Player.x = Window.width/2
Player.y = Window.height/2
Player.w = 25
Player.h = 25
Mainloop.loop = True

Window.obj = pygame.display.set_mode((Window.width,Window.height))

Mainloop.mainloop()

pygame.quit()
