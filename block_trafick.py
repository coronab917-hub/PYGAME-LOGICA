
import pygame
import random
from pathlib import Path

# Inicializar Pygame
pygame.init()

# Configuracion de la ventana
ANCHO = 600
ALTO = 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Block Traffic")

reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (20, 20, 20)
GRIS = (65, 65, 65)
VERDE = (35, 125, 65)
AZUL = (40, 130, 255)
ROJO = (230, 55, 55)
AMARILLO = (255, 220, 50)

# Fuentes
fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 64)
fuente_mediana = pygame.font.Font(None, 44)

# Carretera
LIMITE_IZQUIERDO = 100
LIMITE_DERECHO = 500

# Vehiculos
ANCHO_AUTO = 50
ALTO_AUTO = 80
VELOCIDAD_JUGADOR = 7

# Carriles donde aparecen los enemigos
carriles = [130, 225, 320, 415]

# Archivo para guardar el record
ARCHIVO_RECORD = Path(__file__).with_name("record.txt")


def cargar_record():
    try:
        return int(ARCHIVO_RECORD.read_text().strip())
    except (FileNotFoundError, ValueError):
        return 0


def guardar_record(puntuacion):
    try:
        ARCHIVO_RECORD.write_text(str(puntuacion))
    except OSError:
        print("No se pudo guardar el record.")


def dibujar_texto(texto, fuente_usada, color, x, y):
    imagen = fuente_usada.render(texto, True, color)
    rectangulo = imagen.get_rect(center=(x, y))
    pantalla.blit(imagen, rectangulo)


def reiniciar_juego():
    jugador = pygame.Rect(275, 570, ANCHO_AUTO, ALTO_AUTO)
    enemigos = []
    puntuacion = 0
    velocidad_enemigos = 5
    temporizador = 0

    return jugador, enemigos, puntuacion, velocidad_enemigos, temporizador


def dibujar_carretera():
    pantalla.fill(VERDE)

    pygame.draw.rect(
        pantalla, GRIS,
        (LIMITE_IZQUIERDO, 0, 400, ALTO)
    )

    # Bordes de la carretera
    pygame.draw.line(
        pantalla, BLANCO,
        (LIMITE_IZQUIERDO, 0),
        (LIMITE_IZQUIERDO, ALTO), 5
    )

    pygame.draw.line(
        pantalla, BLANCO,
        (LIMITE_DERECHO, 0),
        (LIMITE_DERECHO, ALTO), 5
    )

    # Lineas de los carriles
    for y in range(-20, ALTO, 100):
        pygame.draw.rect(
            pantalla, AMARILLO,
            (247, y, 5, 45)
        )
        pygame.draw.rect(
            pantalla, AMARILLO,
            (347, y, 5, 45)
        )


def dibujar_juego():
    dibujar_carretera()

    # Dibujar el vehiculo del jugador
    pygame.draw.rect(
        pantalla, AZUL, jugador, border_radius=8
    )

    # Dibujar los enemigos
    for enemigo in enemigos:
        pygame.draw.rect(
            pantalla, ROJO, enemigo, border_radius=8
        )

    # Mostrar puntuacion
    dibujar_texto(
        f"Puntos: {puntuacion}",
        fuente, BLANCO, 65, 30
    )

    # Mostrar record
    dibujar_texto(
        f"Record: {record}",
        fuente, BLANCO, 520, 30
    )


# Variables iniciales
record = cargar_record()

(
    jugador,
    enemigos,
    puntuacion,
    velocidad_enemigos,
    temporizador
) = reiniciar_juego()

estado = "inicio"
ejecutando = True

# Bucle principal
while ejecutando:

    reloj.tick(60)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:

            # Comenzar partida
            if estado == "inicio" and evento.key == pygame.K_SPACE:
                estado = "jugando"

            # Reiniciar partida
            elif estado == "fin" and evento.key == pygame.K_r:
                (
                    jugador,
                    enemigos,
                    puntuacion,
                    velocidad_enemigos,
                    temporizador
                ) = reiniciar_juego()

                estado = "jugando"

            # Volver al inicio
            elif estado == "fin" and evento.key == pygame.K_ESCAPE:
                (
                    jugador,
                    enemigos,
                    puntuacion,
                    velocidad_enemigos,
                    temporizador
                ) = reiniciar_juego()

                estado = "inicio"

    # Logica del juego
    if estado == "jugando":

        teclas = pygame.key.get_pressed()

        # Movimiento horizontal
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jugador.x -= VELOCIDAD_JUGADOR

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jugador.x += VELOCIDAD_JUGADOR

        # Movimiento vertical
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            jugador.y -= VELOCIDAD_JUGADOR

        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            jugador.y += VELOCIDAD_JUGADOR

        # Limitar el carro a la carretera
        jugador.left = max(
            LIMITE_IZQUIERDO,
            min(jugador.left, LIMITE_DERECHO - ANCHO_AUTO)
        )

        # Evitar que salga por arriba o abajo
        jugador.top = max(
            0,
            min(jugador.top, ALTO - ALTO_AUTO)
        )

        # Generar enemigos
        temporizador += 1
        intervalo = max(20, 45 - puntuacion)

        if temporizador >= intervalo:

            x_enemigo = random.choice(carriles)

            enemigo = pygame.Rect(
                x_enemigo, -ALTO_AUTO,
                ANCHO_AUTO, ALTO_AUTO
            )

            enemigos.append(enemigo)
            temporizador = 0

        # Mover enemigos y detectar colisiones
        for enemigo in enemigos[:]:

            enemigo.y += velocidad_enemigos

            # Sumar punto cuando el enemigo sale
            if enemigo.top > ALTO:

                enemigos.remove(enemigo)
                puntuacion += 1

                # Incrementar dificultad
                velocidad_enemigos = min(
                    5 + puntuacion // 3, 18
                )

            # Detectar choque
            elif jugador.colliderect(enemigo):

                estado = "fin"

                # Guardar record si se supera
                if puntuacion > record:
                    record = puntuacion
                    guardar_record(record)

                break

    # Pantalla de inicio
    if estado == "inicio":

        dibujar_carretera()

        dibujar_texto(
            "BLOCK TRAFFIC",
            fuente_grande, AMARILLO,
            ANCHO // 2, 200
        )

        dibujar_texto(
            "Esquiva los vehiculos",
            fuente, BLANCO,
            ANCHO // 2, 280
        )

        dibujar_texto(
            "Flechas o W, A, S, D para moverte",
            fuente, BLANCO,
            ANCHO // 2, 340
        )

        dibujar_texto(
            "Presiona ESPACIO para comenzar",
            fuente, AMARILLO,
            ANCHO // 2, 430
        )

        dibujar_texto(
            f"Record: {record}",
            fuente_mediana, BLANCO,
            ANCHO // 2, 500
        )

    else:

        dibujar_juego()

        # Pantalla de fin de partida
        if estado == "fin":

            capa = pygame.Surface((ANCHO, ALTO))
            capa.set_alpha(180)
            capa.fill(NEGRO)
            pantalla.blit(capa, (0, 0))

            dibujar_texto(
                "¡CHOCASTE!",
                fuente_grande, ROJO,
                ANCHO // 2, 260
            )

            dibujar_texto(
                f"Puntuacion: {puntuacion}",
                fuente_mediana, BLANCO,
                ANCHO // 2, 330
            )

            dibujar_texto(
                f"Record: {record}",
                fuente_mediana, AMARILLO,
                ANCHO // 2, 380
            )

            dibujar_texto(
                "Presiona R para volver a jugar",
                fuente, BLANCO,
                ANCHO // 2, 450
            )

            dibujar_texto(
                "ESC para volver al inicio",
                fuente, BLANCO,
                ANCHO // 2, 495
            )

    pygame.display.flip()

pygame.quit()

