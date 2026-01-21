import sprites
import pygame
import random

WIDTH = 500
HEIGHT = 500

# --- Классы сцен ---
class Scene:
    # обработка событий
    def handle_events(self, events):
        pass
    
    # обновление спрайтов
    def update(self):
        pass
    
    # отрисовка всех игровых объектов
    def draw(self, screen):
        pass
    
class StartScene(Scene):
    def draw(self, screen):
        screen.fill((30, 30, 30))
        font = pygame.font.SysFont('Arial', 32)
        text = font.render(f"Start (ENTER)", True, (255, 255, 255))
        screen.blit(text, (100, 200))
        
    # обновление спрайтов
    def update(self):
        pass
    
    # обработка событий
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return GameScene()
        return self
                
class GameScene(Scene):
    def __init__(self):
        self.cat = sprites.Cat()
        self.bowl = sprites.Bowl()
        self.bowl.rect.x = WIDTH - 64
        self.bowl.rect.y = random.randint(0, HEIGHT)
        self.speed = 5
        self.MOVE_BOWL = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MOVE_BOWL, 300) # 3 раза в секунду
        
    def draw(self, screen):
        screen.fill((0, 150, 15))
        screen.blit(self.cat.surf, self.cat.rect) 
        screen.blit(self.bowl.surf, self.bowl.rect) 
    
    # обновление спрайтов
    def update(self):
        self.cat.update()        
        self.bowl.update()
    
    # обработка событий
    def handle_events(self, events):
        for event in events:
            if event.type == self.MOVE_BOWL:
                self.bowl.rect.x -= self.speed
                if self.bowl.rect.x <= 0:
                    self.bowl.rect.x = WIDTH - 64
                    self.bowl.rect.y = random.randint(0, HEIGHT)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return StartScene()
                
                if event.key == pygame.K_UP:
                    self.cat.rect.y -= self.speed
                
                if event.key == pygame.K_DOWN:
                    self.cat.rect.y += self.speed
                    
        return self