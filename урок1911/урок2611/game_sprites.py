import pygame
from random import*

WIDTH = 600
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    # Конструктор класса
    def __init__(self):
        # Вызов базового конструктора
        super(Player, self).__init__()
        # Загрузка изображения, настройка альфа-канал для прозрачности
        self.surf = pygame.image.load('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок2611/player.png').convert_alpha()
        # Добавление прямоугольника для перемещения объекта
        self.rect = self.surf.get_rect()
        
    def update(self, pos):
        # Меняем координаты спрайта на координаты pos, которые получили из вне
        self.rect.center = pos


class BaseCoin(pygame.sprite.Sprite):
    # Конструктор класса
    def __init__(self, imageName):
        # Вызов базового конструктора
        super(BaseCoin, self).__init__()
        # Загрузка изображения, настройка альфа-канал для прозрачности
        self.surf = pygame.image.load(imageName).convert_alpha()
        # Добавление прямоугольника для перемещения объекта
        self.rect = self.surf.get_rect(center=(randint(16, WIDTH-16), randint(16, HEIGHT-16)))


class Coin(BaseCoin):
    # Конструктор класса
    def __init__(self):
        # Вызов базового конструктора
        super().__init__('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок2611/coin.png')

 
# бонусная монета живет 2секунды, дает в 5 раз больше очков чем обычная монета
# появляется раз в 10 секунд
class BonusCoin(BaseCoin):
    # Конструктор класса
    def __init__(self):
        # Вызов базового конструктора
        super().__init__('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок2611/bonus.png')
       
# живет 3 секунд, появляется раз в 10 секунд
class DeadCoin(BaseCoin):
    # Конструктор класса
    def __init__(self):
         # Вызов базового конструктора
        super().__init__('C:/Users/momentizm/Documents/Среда.Питон/урок1911/урок2611/deadcoin.png')

 