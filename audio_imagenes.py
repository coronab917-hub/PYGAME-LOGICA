import pygame
from pathlib import Path

# Inicializar Pygame y el modulo de audio
pygame.init()
pygame.mixer.init()

# Configuracion de la ventana (proporcion 4:3)
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Traffic Block - Audio y Secuencia de Imagenes")

reloj = pygame.time.Clock()

# Ruta segura hacia la carpeta Media
CARPETA_MEDIA = Path(__file__).with_name("Media")

# Cargar y reproducir la musica de fondo en bucle
pygame.mixer.music.load(str(CARPETA_MEDIA / "musica.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Cargar y escalar las imagenes de fondo
nombres_imagenes = ["carretera.png", "carretera2.png", "carretera3.png"]
imagenes = []

for nombre in nombres_imagenes:
    ruta = CARPETA_MEDIA / nombre
    img = pygame.image.load(str(ruta)).convert()
    img = pygame.transform.scale(img, (ANCHO, ALTO))
    imagenes.append(img)

# Variables para el temporizador de cambio automatico
indice_actual = 0
TIEMPO_CAMBIO = 2500  # 2.5 segundos en milisegundos
ultimo_cambio = pygame.time.get_ticks()

fuente = pygame.font.Font(None, 32)
ejecutando = True

while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Reto de logica: cambiar imagen cada 2.5 segundos con get_ticks()
    ahora = pygame.time.get_ticks()
    if ahora - ultimo_cambio >= TIEMPO_CAMBIO:
        indice_actual = (indice_actual + 1) % len(imagenes)
        ultimo_cambio = ahora

    # Mostrar la imagen actual en pantalla
    screen.blit(imagenes[indice_actual], (0, 0))

    # Indicador discreto del fondo actual
    texto = fuente.render(
        f"Fondo {indice_actual + 1}/{len(imagenes)}",
        True,
        (255, 255, 255)
    )
    screen.blit(texto, (20, 20))

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
