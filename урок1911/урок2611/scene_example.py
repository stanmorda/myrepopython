import pygame

# --- Классы сцен ---
class Scene:
    """Базовый класс для всех сцен."""
    # обработка событий
    def handle_events(self, events):
        pass
    
    # обновление спрайтов
    def update(self):
        pass
    
    # отрисовка всех игровых объектов
    def draw(self, screen):
        pass

class MenuScene(Scene):
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return GameScene() # Переход в игру по Enter
        return self

    def draw(self, screen):
        screen.fill((30, 30, 30))
        font = pygame.font.SysFont('Arial', 32)
        text = font.render("...", True, (255, 255, 255))
        screen.blit(text, (100, 200))

    def update(self):
        pass

class GameScene(Scene):
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return MenuScene() # Возврат в меню по Esc
        return self

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 50, 0))
        font = pygame.font.SysFont('Arial', 24)
        text = font.render("ИГРА ИДЕТ... (Esc для меню)", True, (255, 255, 255))
        screen.blit(text, (10, 10))

# --- Главный менеджер ---

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

scene = MenuScene() # Стартовая сцена

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    # Менеджер меняет сцену, если метод вернул новый объект
    new_scene = scene.handle_events(events)
    if new_scene:
        scene = new_scene

    scene.update()
    scene.draw(screen)

    pygame.display.flip()
    clock.tick(60)
