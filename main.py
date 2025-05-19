import pygame
import random
import sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загрузка изображений
try:
    icon = pygame.image.load(r"C:/Users/user/Documents/GitHub/Tir-game/img/icon.jpeg")
    pygame.display.set_icon(icon)
except:
    print("Иконка не загружена")

try:
    target_img = pygame.image.load(r"C:/Users/user/Documents/GitHub/Tir-game/img/goal.png")
    target_img = pygame.transform.scale(target_img, (160, 160))
    target_width, target_height = 160, 160
except Exception as e:
    print(f"Ошибка загрузки цели: {e}")
    target_img = pygame.Surface((160, 160))
    target_img.fill((0, 255, 0))
    target_width, target_height = 160, 160

# Игровые переменные
score = 0
font = pygame.font.SysFont('Arial', 36)
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    screen.fill(color)

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Отображение счёта
    score_text = font.render(f'Очки: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_x < mouse_x < target_x + target_width and
                    target_y < mouse_y < target_y + target_height):
                score += 1  # Увеличиваем счёт при попадании
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

pygame.quit()
sys.exit()