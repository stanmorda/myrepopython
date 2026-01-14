# На экране будет присутствовать главный персонаж в виде графического объекта, управляемого мышью. 
# С определенными интервалами времени на экране будут появляться монеты. 
# Если персонаж пересекается с монетой или поднимает ее, игрок получает 10 очков.
# Постепенно монеты будут появляться все быстрее, что делает игру более сложной. 
# Игра завершается, когда на экране находится более десяти монет или если игрок закрывает окно
from game_scene import*

pygame.init()
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=[WIDTH, HEIGHT])
# Скрыть курсор мыши
pygame.mouse.set_visible(False)

scene = MenuScene(0) # Стартовая сцена

# coin_pickup_sound = pygame.mixer.Sound('coin_pickup.wav')
# coin_pickup_sound.play()

while running:      
    events = pygame.event.get()
    # Проверка всех доступных событий
    for event in events:
        # Событие закрытия окна
        if event.type == pygame.QUIT:
            running = False
    
    # Менеджер меняет сцену, если метод вернул новый объект
    new_scene = scene.handle_events(events)
    if new_scene:
        scene = new_scene
    is_play = scene.update()

    if not is_play:
        scene = MenuScene(scene.score)
        
    scene.draw(screen)

    # Отображение всех элементов на экране
    pygame.display.flip()
    # Установка игрового таймера
    clock.tick(30)

# Открыть курсор мыши
pygame.mouse.set_visible(True)
pygame.quit()
