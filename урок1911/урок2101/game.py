import scenes
import pygame

pygame.init()
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=[scenes.WIDTH, scenes.HEIGHT])
scene = scenes.StartScene()

while running:
    events = pygame.event.get()
    # Проверка всех доступных событий
    for event in events:
        # Событие закрытия окна
        if event.type == pygame.QUIT:
            running = False
            
    scene = scene.handle_events(events)

    scene.update()
    scene.draw(screen)
    
    pygame.display.flip()
    
    clock.tick()