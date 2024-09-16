# game.py
import pygame
import random
from constants import WIDTH, HEIGHT, WHITE, BLACK, GRAVITY
from dinosaur import Dinosaur  # Import the Dinosaur class

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chrome Dinosaur Game")
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.menu_active = True
        self.score = 0
        self.frame_count = 0
        self.dino = Dinosaur()
        self.obstacles = []

    def create_obstacle(self):
        obstacle_surface = pygame.Surface((20, 40))
        obstacle_surface.fill(BLACK)
        obstacle_rect = obstacle_surface.get_rect(midbottom=(random.randint(900, 1100), HEIGHT - 30))
        return obstacle_rect

    def move_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.x -= 5
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.x > -20]

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            self.screen.blit(pygame.Surface((20, 40)), obstacle)

    def check_collision(self):
        for obstacle in self.obstacles:
            if self.dino.rect.colliderect(obstacle):
                return False
        return True

    def display_menu(self):
        self.screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text = font.render('Press SPACE to Start', True, BLACK)
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()

    def display_game_over(self):
        self.screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over. Press space to restart.', True, BLACK)
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()

    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_surface = font.render(f'Score: {self.score}', True, BLACK)
        self.screen.blit(score_surface, (10, 10))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.menu_active:
                            self.menu_active = False
                            self.game_active = True
                            self.score = 0
                            self.obstacles = []
                            self.dino.reset()
                        elif not self.game_active:
                            self.game_active = True
                            self.score = 0
                            self.obstacles = []
                            self.dino.reset()
                        elif self.game_active and self.dino.rect.bottom >= HEIGHT - 30:
                            self.dino.jump()

            if self.menu_active:
                self.display_menu()
            elif self.game_active:
                self.dino.update()
                self.move_obstacles()
                if random.randint(0, 60) == 0:
                    self.obstacles.append(self.create_obstacle())
                self.game_active = self.check_collision()
                self.frame_count += 1
                if self.frame_count % 10 == 0:
                    self.score += 1
                self.screen.fill(WHITE)
                self.dino.draw(self.screen)
                self.draw_obstacles()
                self.display_score()
            else:
                self.display_game_over()

            pygame.display.update()
            self.clock.tick(60)