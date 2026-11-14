#  Traffic Block

**Estudiante:** Benjamín Corona Pacheco

**Objetivo general del juego:** 
Traffic Block es un juego tipo arcade donde el jugador controla un bloque principal que avanza por una calle. El objetivo es esquivar los demás bloques (que simulan el tráfico o los obstáculos) para sobrevivir el mayor tiempo posible y alcanzar la máxima puntuación
## Investigación sobre Pygame

### 1. ¿Qué es Pygame y para qué se utiliza?
[Pygame](https://www.pygame.org/docs/tut/PygameIntro.html) es una biblioteca de Python construida sobre **SDL (Simple DirectMedia Layer)**, una librería multiplataforma en C orientada a multimedia. Se utiliza principalmente para desarrollar videojuegos 2D, prototipos interactivos y simulaciones gráficas, ya que facilita el control de ventanas, gráficos, teclado, ratón, tiempos y audio sin tener que programar todo desde cero a bajo nivel.

### 2. Relación de Pygame con los temas vistos en clase
En el desarrollo de **Block Traffic** (`block_trafick.py`), Pygame aplica directamente los fundamentos de programación:
- **Ciclos (`while` y `for`):** El juego corre dentro de un bucle principal (`while ejecutando:`) controlado a 60 FPS con `reloj.tick(60)`, además de ciclos `for` para recorrer eventos, dibujar líneas de carriles y mover cada enemigo.
- **Eventos y condicionales (`if/elif`):** Con `pygame.event.get()` y `pygame.key.get_pressed()` se detectan teclas (flechas, WASD, `ESPACIO`, `R`, `ESC`) y el cierre de la ventana (`pygame.QUIT`) para cambiar entre los estados `"inicio"`, `"jugando"` y `"fin"`.
- **Estructuras de datos:** Se usan **listas** (`carriles` y `enemigos`) para almacenar posiciones y obstáculos activos en pantalla, y **tuplas** para definir colores RGB (`(255, 255, 255)`) y dimensiones.
- **Funciones:** El código se organiza en bloques reutilizables como `cargar_record()`, `guardar_record()`, `reiniciar_juego()`, `dibujar_carretera()` y `dibujar_juego()`.

### 3. ¿Qué significa que Pygame permite "tomar mucho o poco" de la librería?
Significa que [Pygame es modular](https://www.pygame.org/docs/tut/PygameIntro.html): no te obliga a usar un motor rígido ni todas sus herramientas a la vez. Puedes tomar **poco** (por ejemplo, usar solo `display`, `draw`, `event`, `Rect` y `font`, como en `block_trafick.py`) o tomar **mucho** conforme crece el proyecto (agregando módulos más avanzados como [`sprite`](https://www.pygame.org/docs/tut/SpriteIntro.html) para agrupar personajes, `image` para cargar texturas o `mixer` para música y efectos de sonido).

## Flujo de trabajo con ramas

El repositorio `PYGAME-LOGICA` se organiza con las siguientes ramas:
- **`main`:** Contiene la versión estable y documentada del proyecto lista para entrega.
- **`v01`:** Rama de integración y desarrollo de la versión actual del juego (**Block Traffic**). Desde aquí se hacen `merge` hacia `main` cuando una versión queda probada.
- **`actividad1`:** Almacena las prácticas iniciales de Pygame (`juegos.py`, `mejora.py`, `microproyecto.py`).
- **`actividad2`:** Almacena la evolución hacia el proyecto integrador (`block_trafick.py` y `record.txt`).
