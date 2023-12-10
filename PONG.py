import pygame, sys
pygame.init()
#prueba
#Definiendo variables
ancho, alto= (800, 600)
size= (ancho, alto)
fps= pygame.time.Clock()
negro=( 0, 0, 0)
blanco=(255, 255, 255)
verde=(0, 255, 0)
rojo= (255, 0, 0)

#Tamaños jugadores
ejexy_1=[10, 194]
ejexy_1end=[10, 348]

ejexy_2=[790, 194]
ejexy_2end=[790, 348]

pelota_pos=[ancho // 2, alto // 2]
pelota_rad=20

pelota_vel=[5, 5]

#Ventana
ventana=pygame.display.set_mode(size)
#Configuracion de ventana
ventana.fill(blanco)




while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

#Para garantizar que la pelota borre el rastro
    ventana.fill(blanco)

#movimiento
    pelota_pos[0] += pelota_vel[0]
    pelota_pos[1] += pelota_vel[1]

#colision pared
    if pelota_pos[1] <= 0 or pelota_pos[1] >= 600:
        pelota_vel[1] *= -1
    #if pelota_pos[0] <= 0 or pelota_pos[0] >= 800:
     #   pelota_vel[0] *= -1


#pulsasiones de teclas mediante array get pressed y evitar que las paletas salgan de la pantalla
    #J1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] == 1 and ejexy_1[1] >= 0:
        ejexy_1[1] -= 10
        ejexy_1end[1] -= 10
    if keys[pygame.K_s] == 1 and ejexy_1end[1] <=600:
        ejexy_1[1] += 10
        ejexy_1end[1] += 10
    #J2
    if keys[pygame.K_UP] == 1 and ejexy_2[1] >= 0:
        ejexy_2[1] -= 10
        ejexy_2end[1] -= 10
    if keys[pygame.K_DOWN] == 1 and ejexy_2end[1] <= 600:
        ejexy_2[1] += 10
        ejexy_2end[1] += 10

#Definicion de controles para reiniciar o aumentar y disminuir velocidad
    if keys[pygame.K_r] == 1:
        pelota_pos=[ancho // 2, alto // 2]
        pelota_vel=[0, 0]

    if keys[pygame.K_SPACE] == 1:
        pelota_vel = [5, 5]

 #ZONA DE DIBUJO
    jugador1=pygame.draw.line(ventana, rojo, (ejexy_1[0], ejexy_1[1]), (ejexy_1end[0], ejexy_1end[1]), 15)

    pygame.draw.circle(ventana, negro, (int(pelota_pos[0]), int(pelota_pos[1])), pelota_rad)
    
    jugador2=pygame.draw.line(ventana, verde, (ejexy_2[0], ejexy_2[1]), (ejexy_2end[0], ejexy_2end[1]), 15)

#colison paleta pelota
    if ejexy_1[0] <= pelota_pos[0] <= ejexy_1end[0] and ejexy_1[1] - pelota_rad <= pelota_pos[1] <= ejexy_1end[1] + pelota_rad: 
        pelota_vel[0] *= -1
    if ejexy_2[0] <= pelota_pos[0] <= ejexy_2end[0] and ejexy_2[1] - pelota_rad <= pelota_pos[1] <= ejexy_2end[1] + pelota_rad: 
        pelota_vel[0] *= -1

#ZONA DE DIBUJO
    pygame.display.flip()
    fps.tick(60)