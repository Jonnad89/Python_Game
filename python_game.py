import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana del juego
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Juego con PyGame')

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Reloj para controlar la velocidad de actualización de la pantalla
clock = pygame.time.Clock()

# Funciones
def draw_player(x, y):
    pygame.draw.rect(game_window, red, [x, y, 50, 50])

def draw_enemy(x, y):
    pygame.draw.rect(game_window, black, [x, y, 30, 30])

# Posiciones iniciales del jugador y del enemigo
player_x = window_width // 2
player_y = window_height - 100
enemy_x = random.randint(0, window_width - 30)
enemy_y = 0

# Velocidad del jugador y del enemigo
player_speed = 5
enemy_speed = 3

# Inicialización del puntaje
score = 0

# Variable para controlar la pausa
paused = False

# Bucle principal del juego
running = True
while running:
    game_window.fill(white)  # Limpia la ventana

    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                paused = not paused  # Cambia el estado de pausa

    if not paused:  # Si no está en pausa, el juego continúa

        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < window_width - 50:
            player_x += player_speed

        # Dibujar jugador y enemigo
        draw_player(player_x, player_y)
        draw_enemy(enemy_x, enemy_y)

        # Movimiento del enemigo
        enemy_y += enemy_speed
        if enemy_y > window_height:
            enemy_x = random.randint(0, window_width - 30)
            enemy_y = 0

        # Colisión entre jugador y enemigo
        if player_x < enemy_x + 30 and player_x + 50 > enemy_x and player_y < enemy_y + 30 and player_y + 50 > enemy_y:
            # Imprime un mensaje de colisión
            print("¡Colisión!")

            # Incrementa el puntaje en 1
            score += 1

            # Restablece la posición del enemigo
            enemy_x = random.randint(0, window_width - 30)
            enemy_y = 0

        # Mostrar puntaje en la ventana del juego
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Puntaje: {score}", True, black)
        game_window.blit(score_text, (10, 10))

    else:
        # Mostrar mensaje de pausa
        font = pygame.font.Font(None, 48)
        paused_text = font.render("Juego en pausa", True, black)
        game_window.blit(paused_text, (window_width // 2 - 150, window_height // 2 - 30))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
