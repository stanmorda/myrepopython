# Импортируем библиотеку и инициализируем

import pygame

# Случайное размещение монет

from random import randint

# Поиск ресурсов

from pathlib import Path

# Аннотация типов

from typing import Tuple

# Установка размеров окна

WIDTH = 800

HEIGHT = 600

# Настройка частоты появления монет (мс)

coin_countdown = 2500

coin_interval = 100

# Максимальное количество монет на экране для завершения игры

COIN_COUNT = 10

# Определяем вид графического объекта для игрока

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        # Определение изображения персонажа

        player_image = str('alien_green_stand.png')

        # Загрузка изображения, настройка альфа-канал для прозрачности

        self.surf = pygame.image.load(player_image).convert_alpha()

    # Добавление прямоугольника для перемещения объекта

        self.rect = self.surf.get_rect()

    def update(self, pos: Tuple):

        self.rect.center = pos

# Определение графического изображения для монет

class Coin(pygame.sprite.Sprite):

    def __init__(self):


        super(Coin, self).__init__()

        # Определение изображения монеты

        coin_image = str('coin_gold.png')

        # Загрузка изображения, настройка альфа-канала для прозрачности

        self.surf = pygame.image.load(coin_image).convert_alpha()

        # Определение позиция для старта, генерация случайной позиции

        # self.rect = self.surf.get_rect(randint(10, WIDTH — 10),randint(10, HEIGHT — 10))

# Инициализация движка

pygame.init()

# Настройка окна

screen = pygame.display.set_mode(size=[WIDTH, HEIGHT])

# Скрыть курсор мыши

pygame.mouse.set_visible(False)

# Запуск часов для фиксации времени

clock = pygame.time.Clock()

# Создание события для добавления монеты

ADDCOIN = pygame.USEREVENT + 1

pygame.time.set_timer(ADDCOIN, coin_countdown)

# Настройка списка монет

coin_list = pygame.sprite.Group()


score = 0

# Установка звука для сбора монет

# coin_pickup_sound = pygame.mixer.Sound('coin_pickup.wav')

# Создание графического изображения игрока и установка на позицию старта

player = Player()

player.update(pygame.mouse.get_pos())

# Запуск цикла событий

running = True

while running:

# Проверка, нажал ли пользователь кнопку закрытия окна

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # Определение условий для добавления монеты

        elif event.type == ADDCOIN:

        # Добавление новой монеты

            new_coin = Coin()

            coin_list.add(new_coin)

        # Ускорение игры при наличии менее трех монет на экране

        if len(coin_list) < 3:

            coin_countdown -= coin_interval

        # Установка ограничения скорости

        if coin_countdown < 100:

            coin_countdown = 100

        # Остановка таймера

        pygame.time.set_timer(ADDCOIN, 0)


        # Запуск нового таймера

        pygame.time.set_timer(ADDCOIN, coin_countdown)

        # Обновление позиции персонажа

        player.update(pygame.mouse.get_pos())

        # Проверка, собрал ли герой монету и удаление, если да

        coins_collected = pygame.sprite.spritecollide(

        sprite=player, group=coin_list, dokill=True

        )

        for coin in coins_collected:

            # Установка счета за собранные монеты

            score += 10

            # Воспроизведение звука для сбора монеты

            # coin_pickup_sound.play()

            # Проверка допустимого количества монет

            if len(coin_list) >= COIN_COUNT:

            # Если лимит превышен, игра останавливается

                running = False

            # Установка цвета фона

            screen.fill((255, 170, 164))

            # Отрисовка монеты

            for coin in coin_list:

                screen.blit(coin.surf, coin.rect)

                # Отрисовка персонажа

                screen.blit(player.surf, player.rect)

                # Вывод текущего счета

                score_font = pygame.font.SysFont('any_font', 36)

                score_block = score_font.render(f'Score: {score}', False, (0, 0, 0))

                # screen.blit(score_block, (50, HEIGHT — 50))

        # Отображение всех элементов на экране

        pygame.display.flip()

        # Установка скорости обновления

        clock.tick(30)

        # Вывод итогового результата



        # Возврат видимости курсора

        pygame.mouse.set_visible(True)

# Выход из игры

pygame.quit()