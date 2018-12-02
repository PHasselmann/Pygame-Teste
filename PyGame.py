# -*- coding: utf-8 -*-
import pygame
import random

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

velox=0.2 
veloy=0.2

pygame.init()

l=640
a=480
tamanho=10
posx=random.randint(0, (l-tamanho)/10)*10
posy=random.randint(0, (a-tamanho)/10)*10

fundo=pygame.display.set_mode((l,a))
pygame.display.set_caption("carros")

sair=True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair= False
            
            
    fundo.fill(preto)
    
    
    
    
    pygame.draw.rect(fundo, branco, [50,posy, 25, 50])
    pygame.draw.rect(fundo, branco, [0+200,posy, 25, 50])
    pygame.draw.rect(fundo, branco, [0+400,posy, 25, 50])
    pygame.draw.rect(fundo, branco, [posx,20, 50, 25])
    pygame.draw.rect(fundo, branco, [posx,200, 50, 25])
    pygame.draw.rect(fundo, branco, [posx,350, 50, 25])
    
    posy-=veloy
    posx+=velox
    
    if posy>480:
        posy=0
        
    if posy<0:
        posy=480
        
    if posx>640:
        posx=0
        
    if posx<0:
        posx=640 
    pygame.display.update()

pygame.quit()