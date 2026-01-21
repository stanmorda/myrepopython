import pygame

# создать два спрайта : корм, игрок-кот

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        # Вызов базового конструктора
        super(Cat, self).__init__()
        
        # Загрузка изображения, настройка альфа-канал для прозрачности
        self.surf = pygame.image.load('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок2101/cat.png').convert_alpha()
        
        # Добавление прямоугольника для перемещения объекта
        self.rect = self.surf.get_rect()
    
    def update(self):
        pass
        
        
class Bowl(pygame.sprite.Sprite):
    def __init__(self):
        # Вызов базового конструктора
        super(Bowl, self).__init__()
        
        # Загрузка изображения, настройка альфа-канал для прозрачности
        self.surf = pygame.image.load('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок2101/bowl.png').convert_alpha()
        
        # Добавление прямоугольника для перемещения объекта
        self.rect = self.surf.get_rect()
        
    def update(self):
        pass