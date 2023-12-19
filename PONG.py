import pygame, sys
pygame.init()
#prueba
#Definiendo variables
ancho, alto = (800, 600)
size = (ancho, alto)
fps = pygame.time.Clock()
negro =( 0, 0, 0)
blanco =(255, 255, 255)
verde =(0, 255, 0)
rojo = (255, 0, 0)
gris = (128, 128, 128)

#Tamaños jugadores
ejexy_1 = [10, 194]
ejexy_1end = [10, 348]

ejexy_2 = [790, 194]
ejexy_2end = [790, 348]

pelota_pos = [ancho // 2, alto // 2]
pelota_rad=20

pelota_vel = [5, 5]

#Ventana
ventana = pygame.display.set_mode(size)

#Definiendo formato de texto
fuente = pygame.font.Font(None, 20)
pJugador1 = "Puntaje J1:"
pJugador2 = "Puntaje J2:"
imp_J1 = fuente.render(pJugador1, 1, (negro))
imp_J2 = fuente.render(pJugador2, 1, (negro))

Puntaje_J1 = 0
Puntaje_J2 = 0

if ejexy_2[0] <= pelota_pos[0] <= ejexy_2end[0] and ejexy_2[1] - pelota_rad <= pelota_pos[1] <= ejexy_2end[1] + pelota_rad: 
    pelota_vel[0] *= -1
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    imp_PTJ1 = fuente.render(str(Puntaje_J1), 1, (negro))
    imp_PTJ2 = fuente.render(str(Puntaje_J2), 1, (negro))

#Para garantizar que la pelota borre el rastro
    ventana.fill(blanco)

#movimiento
    pelota_pos[0] += pelota_vel[0]
    pelota_pos[1] += pelota_vel[1]

#colision pared
    if pelota_pos[1] <= 0 or pelota_pos[1] >= 600:
        pelota_vel[1] *= -1

#pulsasiones de teclas mediante array get pressed y evitar que las paletas salgan de la pantalla
    #J1
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

#Definicion de controles y demas funcionalidades
    if keys[pygame.K_r] == 1:
        pelota_pos=[ancho // 2, alto // 2]
        pelota_vel=[0, 0]

    if keys[pygame.K_SPACE] == 1:
        pelota_vel = [5, 5]

    if pelota_pos [0] <= -40:
        pelota_pos=[ancho // 2, alto // 2]
        pelota_vel=[0, 0]
        Puntaje_J2 += 1

    if pelota_pos [0] >= 840:
        pelota_pos=[ancho // 2, alto // 2]
        pelota_vel=[0, 0]
        Puntaje_J1 += 1

 #ZONA DE DIBUJO
    jugador1=pygame.draw.line(ventana, rojo, (ejexy_1[0], ejexy_1[1]), (ejexy_1end[0], ejexy_1end[1]), 15)

    pygame.draw.circle(ventana, negro, (int(pelota_pos[0]), int(pelota_pos[1])), pelota_rad)
    
    jugador2=pygame.draw.line(ventana, verde, (ejexy_2[0], ejexy_2[1]), (ejexy_2end[0], ejexy_2end[1]), 15)

    red = pygame.draw.line(ventana, gris, (ancho //2, 0), (ancho //2, 600), 3)

    ventana.blit(imp_J1, (20, 0))
    ventana.blit(imp_J2, (705, 0))

    ventana.blit(imp_PTJ1,(95, 0))
    ventana.blit(imp_PTJ2, (780, 0))

#colison paleta pelota
    if ejexy_1[0] <= pelota_pos[0] <= ejexy_1end[0] and ejexy_1[1] - pelota_rad <= pelota_pos[1] <= ejexy_1end[1] + pelota_rad: 
        pelota_vel[0] *= -1
    if ejexy_2[0] <= pelota_pos[0] <= ejexy_2end[0] and ejexy_2[1] - pelota_rad <= pelota_pos[1] <= ejexy_2end[1] + pelota_rad: 
        pelota_vel[0] *= -1

#ZONA DE DIBUJO
    pygame.display.flip()
    fps.tick(60)