
import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primer videojuego")

negro = (0, 0, 0)
azul = (0, 100, 255)

x = 375
y = 275
velocidad = 5

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    ventana.fill(negro)
    pygame.draw.rect(ventana, azul, (x, y, 50, 50))

    pygame.display.update()
    reloj.tick(60)

pygame.quit()
