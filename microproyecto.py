
import pygame
import random

# 1. Inicializar Pygame
pygame.init()

# 2. Configurar la ventana
ANCHO = 600
ALTO = 700

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Block Traffic")

reloj = pygame.time.Clock()

# 3. Definir colores
NEGRO = (20, 20, 20)
BLANCO = (255, 255, 255)
GRIS = (65, 65, 65)
AZUL = (0, 120, 255)
ROJO = (240, 50, 50)
AMARILLO = (255, 220, 0)
VERDE = (30, 200, 100)

# 4. Crear textos
fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 60)

# 5. Configurar la carretera
carretera_izq = 100
carretera_der = 500
ancho_carretera = carretera_der - carretera_izq

# 6. Crear al jugador
ancho_carro = 50
alto_carro = 80

jugador = pygame.Rect(
    ANCHO // 2 - ancho_carro // 2,
    ALTO - 120,
    ancho_carro,
    alto_carro
)

velocidad_jugador = 6

# 7. Crear los vehículos enemigos
enemigos = []
velocidad_enemigos = 5
tiempo_aparicion = 0

# 8. Variables del juego
puntuacion = 0
juego_activo = True
juego_terminado = False

# Posiciones de los carriles
carriles = [180, 275, 370]


# 9. Ciclo principal
while juego_activo:

    # Controlar la velocidad del juego
    reloj.tick(60)

    # Revisar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_activo = False

        # Reiniciar con la tecla R después de perder
        if evento.type == pygame.KEYDOWN:
            if juego_terminado and evento.key == pygame.K_r:

                jugador.x = ANCHO // 2 - ancho_carro // 2
                enemigos.clear()

                puntuacion = 0
                velocidad_enemigos = 5
                tiempo_aparicion = 0

                juego_terminado = False

    # Ejecutar la lógica mientras la partida esté activa
    if not juego_terminado:

        # Leer las teclas presionadas
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            jugador.x -= velocidad_jugador

        if teclas[pygame.K_RIGHT]:
            jugador.x += velocidad_jugador

        # Mantener al jugador dentro de la carretera
        if jugador.left < carretera_izq:
            jugador.left = carretera_izq

        if jugador.right > carretera_der:
            jugador.right = carretera_der

        # Generar enemigos cada cierto tiempo
        tiempo_aparicion += 1

        if tiempo_aparicion >= 45:
            carril = random.choice(carriles)

            enemigo = pygame.Rect(
                carril,
                -alto_carro,
                ancho_carro,
                alto_carro
            )

            enemigos.append(enemigo)
            tiempo_aparicion = 0

        # Mover los enemigos
        for enemigo in enemigos[:]:
            enemigo.y += velocidad_enemigos

            # Si el enemigo sale de la pantalla,
            # aumentar la puntuación
            if enemigo.top > ALTO:
                enemigos.remove(enemigo)
                puntuacion += 1

            # Detectar colisión con el jugador
            elif jugador.colliderect(enemigo):
                juego_terminado = True

        # Aumentar un poco la dificultad
        velocidad_enemigos = min(5 + puntuacion // 3, 18)

    # 10. Dibujar el fondo
    ventana.fill(VERDE)

    # Dibujar la carretera
    pygame.draw.rect(
        ventana,
        GRIS,
        (carretera_izq, 0, ancho_carretera, ALTO)
    )

    # Dibujar los bordes de la carretera
    pygame.draw.line(
        ventana, BLANCO,
        (carretera_izq, 0),
        (carretera_izq, ALTO), 5
    )

    pygame.draw.line(
        ventana, BLANCO,
        (carretera_der, 0),
        (carretera_der, ALTO), 5
    )

    # Dibujar líneas discontinuas entre carriles
    for y_linea in range(0, ALTO, 100):
        pygame.draw.rect(
            ventana,
            AMARILLO,
            (295, y_linea, 6, 50)
        )

    # Dibujar al jugador
    pygame.draw.rect(
        ventana,
        AZUL,
        jugador,
        border_radius=8
    )

    # Dibujar los vehículos enemigos
    for enemigo in enemigos:
        pygame.draw.rect(
            ventana,
            ROJO,
            enemigo,
            border_radius=8
        )

    # Mostrar puntuación
    texto_puntos = fuente.render(
        f"Puntos: {puntuacion}",
        True,
        BLANCO
    )

    ventana.blit(texto_puntos, (20, 20))

    # Mostrar instrucciones
    texto_controles = fuente.render(
        "Usa las flechas para moverte",
        True,
        BLANCO
    )

    ventana.blit(texto_controles, (120, ALTO - 40))

    # Pantalla de fin de partida
    if juego_terminado:

        mensaje = fuente_grande.render(
            "¡CHOCASTE!",
            True,
            AMARILLO
        )

        reinicio = fuente.render(
            "Presiona R para jugar otra vez",
            True,
            BLANCO
        )

        ventana.blit(
            mensaje,
            mensaje.get_rect(
                center=(ANCHO // 2, ALTO // 2 - 30)
            )
        )

        ventana.blit(
            reinicio,
            reinicio.get_rect(
                center=(ANCHO // 2, ALTO // 2 + 30)
            )
        )

    # Actualizar la pantalla
    pygame.display.update()

# 11. Cerrar Pygame
pygame.quit()
