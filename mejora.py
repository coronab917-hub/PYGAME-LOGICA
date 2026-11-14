
import pygame
import math

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana
ANCHO = 800
ALTO = 600

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de recoleccion")

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 100, 255)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

# Datos del jugador
x = 50
y = 275
tamanio = 50
velocidad = 5

jugador = pygame.Rect(x, y, tamanio, tamanio)

# Crear el objeto que se debe recolectar
objeto = pygame.Rect(600, 280, 40, 40)

# Texto del mensaje
fuente = pygame.font.Font(None, 48)

# Control del juego
reloj = pygame.time.Clock()
ejecutando = True
recolectado = False

# Ciclo principal
while ejecutando:

    # Revisar si se cierra la ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Mover al jugador mientras no recolecte el objeto
    if not recolectado:
        teclas = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if teclas[pygame.K_LEFT]:
            dx -= 1
        if teclas[pygame.K_RIGHT]:
            dx += 1
        if teclas[pygame.K_UP]:
            dy -= 1
        if teclas[pygame.K_DOWN]:
            dy += 1

        # Evitar que el movimiento diagonal sea mas rapido
        if dx != 0 and dy != 0:
            factor = 1 / math.sqrt(2)
        else:
            factor = 1

        x += dx * velocidad * factor
        y += dy * velocidad * factor

        # Evitar que el jugador salga de la ventana
        x = max(0, min(x, ANCHO - tamanio))
        y = max(0, min(y, ALTO - tamanio))

        # Actualizar la posicion del jugador
        jugador.topleft = (round(x), round(y))

        # Detectar la colision con el objeto
        if jugador.colliderect(objeto):
            recolectado = True

    # Dibujar el fondo
    ventana.fill(NEGRO)

    # Dibujar al jugador azul
    pygame.draw.rect(ventana, AZUL, jugador)

    # Mostrar el objeto verde mientras no se recolecte
    if not recolectado:
        pygame.draw.rect(ventana, VERDE, objeto)

    # Mostrar el mensaje al recolectar el objeto
    if recolectado:
        texto = fuente.render(
            "YA ES TODO!!", True, BLANCO
        )
        ventana.blit(texto, (250, 180))

    # Actualizar la pantalla
    pygame.display.update()
    reloj.tick(60)

# Cerrar Pygame
pygame.quit()

