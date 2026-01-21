import sprites
import pygame


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
    
    def draw(self, screen):
        screen.fill((0, 150, 15))
        screen.blit(self.cat.surf, self.cat.rect) 
        screen.blit(self.bowl.surf, self.bowl.rect) 
    
    # обновление спрайтов
    def update(self):
        pass
    
    # обработка событий
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return StartScene()
        return self