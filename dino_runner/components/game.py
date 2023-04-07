import pygame
import random
from dino_runner.components import tex_utils
from dino_runner.utils.constants import BG, CLOUD, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = self.screen.get_width()
        self.y_pos_cloud = random.randint(0, self.screen.get_height() - CLOUD.get_height())
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.dead_counter = 0
        self.dark_mode = False

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.obstacle_manager.obstacles)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.points += 1
            if self.points % 500 == 0:
                self.game_speed += 1
            if self.points >= 600:
                self.dark_mode = True
            if self.player.dino_dead:
                self.playing = False
                self.dead_counter += 1

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            if self.dark_mode:
                self.screen.fill((0, 0, 0))
            else:
                self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_cloud()
            self.player.draw(self.screen)
            self.draw_score()
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()
        
        
        
    def draw_background(self):
        if self.dark_mode:
            self.screen.fill((0, 0, 0))
        else:
            self.screen.fill((255, 255, 255))

        image = BG
        image_width = image.get_width()

        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(image, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.x_pos_cloud -= self.game_speed
        if self.x_pos_cloud <= -image_width:
            self.x_pos_cloud = self.screen.get_width()
            self.y_pos_cloud = random.randint(0, 100)
            
            
    def draw_score(self):
        score, score_rect = tex_utils.get_message('Points: ' + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_rect)
        
    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_element()
        
    def print_menu_element(self):
        if self.dead_counter == 0:
            text, text_rect = tex_utils.get_message('Press any Key to Star', 30)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = tex_utils.get_message('Press any Key to Restar', 30)
            score, score_rect = tex_utils.get_message('Your score: ' + str(self.points), 30, height=SCREEN_HEIGHT//2 +50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
    
    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.dark_mode = False
