import pygame
import random

pygame.init()

WIDTH = 768
HEIGHT = 480
FPS = 75

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (30, 144, 255)  # Azul
BALL_COLOR = (255, 69, 0)  # Vermelho

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

player1_pos = pygame.Rect(50, HEIGHT // 2 - 50, 10, 100)
player2_pos = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed = [7 * random.choice((1, -1)), 7 * random.choice((1, -1))]


def move_ai_paddle(paddle, ball):
    if paddle.centery < ball.centery:
        paddle.centery += 5
    elif paddle.centery > ball.centery:
        paddle.centery -= 5
    return paddle


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1_pos.centery -= 10
    if keys[pygame.K_DOWN]:
        player1_pos.centery += 10

    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(player1_pos) or ball.colliderect(player2_pos):
        ball_speed[0] = -ball_speed[0]

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
        ball.center = (WIDTH // 2, HEIGHT // 2)

    player2_pos = move_ai_paddle(player2_pos, ball)

    # Preencher a tela com a cor de fundo
    screen.fill(BLACK)

    # Desenhar paletas e bola com cores
    pygame.draw.rect(screen, PLAYER_COLOR, player1_pos)
    pygame.draw.rect(screen, PLAYER_COLOR, player2_pos)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
