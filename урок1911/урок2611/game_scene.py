from game_sprites import*

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
    
class MenuScene(Scene):
    
    def __init__(self, lastScore):
        self.lastScore = lastScore
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    return GameScene() # Переход в игру по Enter
        return self

    def draw(self, screen):
        screen.fill((30, 30, 30))
        font = pygame.font.SysFont('Arial', 32)
        text = font.render(f"Start (ENTER)", True, (255, 255, 255))
        screen.blit(text, (100, 200))
        
        if self.lastScore > 0:
            text = font.render(f"Last Score : {self.lastScore}", True, (255, 255, 255))
            screen.blit(text, (150, 250))

    def update(self):
        return True

class GameScene(Scene):
    def __init__(self):
        self.COLOR_FILL = (255, 170, 164)
        self.coin_countdown = 1000 
        self.deadcoin_interval = 10 * 1000
        self.deadcoin_livetime = 3 * 1000
        self.bonus_interval = 10 * 1000
        self.score = 0
        self.score_count = 0
        self.one_coin_cost = 10
    
        self.player = Player()
        self.deadCoin = DeadCoin()
        self.ADDCOIN = pygame.USEREVENT + 1
        self.DEADCOIN = pygame.USEREVENT + 2
        self.DEADCOIN_CLEAR = pygame.USEREVENT + 3
        self.BONUSCOIN = pygame.USEREVENT + 4
        self.BONUSCOIN_CLEAR = pygame.USEREVENT + 5
        
        # Настройка списка монет
        self.coin_list = pygame.sprite.Group()
        # Настройка списка dead - монет
        self.deadcoin_list = pygame.sprite.Group()
        # Настройка списка bonus - монет
        self.bonus_list = pygame.sprite.Group()
            
        # Создание события для добавления монеты
        pygame.time.set_timer(self.ADDCOIN, self.coin_countdown)
        pygame.time.set_timer(self.DEADCOIN, self.deadcoin_interval)
        pygame.time.set_timer(self.BONUSCOIN, self.bonus_interval)
         
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return MenuScene() # Возврат в меню по Esc
                
            # Наше событие ADDCOIN для создания монеты по таймеру
            if event.type == self.ADDCOIN:
                # Добавление новой монеты
                self.coin_list.add(Coin())
                
            if event.type == self.DEADCOIN: # событие на мертвую монету
                self.deadcoin_list.add(DeadCoin())
                pygame.time.set_timer(self.DEADCOIN, 0)
                pygame.time.set_timer(self.DEADCOIN, self.deadcoin_interval)
                pygame.time.set_timer(self.DEADCOIN_CLEAR, int(randint(2, 3) * 1000))
                
            if event.type == self.DEADCOIN_CLEAR: # событие на то чтобы убить мертвую монету спустя 3секунды времени ее жизни
                self.deadcoin_list.empty()
                pygame.time.set_timer(self.DEADCOIN_CLEAR, 0)
                
            if event.type == self.BONUSCOIN: # событие на бонусную монету
                self.bonus_list.add(BonusCoin())
                pygame.time.set_timer(self.BONUSCOIN, 0)
                pygame.time.set_timer(self.BONUSCOIN, self.bonus_interval)
                pygame.time.set_timer(self.BONUSCOIN_CLEAR, int(randint(2, 3) * 1000))
                    
            if event.type == self.BONUSCOIN_CLEAR: # событие на то чтобы убить бонусную монету спустя 3секунды времени ее жизни
                self.bonus_list.empty()
                pygame.time.set_timer(self.BONUSCOIN_CLEAR, 0)   
            
        return self

    def update(self):
        if len(self.coin_list) > 10:
            return False  
       
        # Проверить что игрок коснулся монеты
        coins_collected = pygame.sprite.spritecollide(sprite=self.player, group=self.coin_list, dokill=True)
        for item in coins_collected:    
            self.score += self.one_coin_cost
            if self.coin_countdown > 500:
                self.coin_countdown -= 50
                pygame.time.set_timer(self.ADDCOIN, 0) # остановили таймер
                pygame.time.set_timer(self.ADDCOIN, self.coin_countdown) # запустили новый таймер

        
        deadcoins_collected = pygame.sprite.spritecollide(sprite=self.player, group=self.deadcoin_list, dokill=True)
        if len(deadcoins_collected) > 0:
            return False
            
        bonus_collected = pygame.sprite.spritecollide(sprite=self.player, group=self.bonus_list, dokill=True)
        if len(bonus_collected) > 0:
            self.score += self.one_coin_cost * 5
            # обновим таймеры жизни бонусной монеты
            pygame.time.set_timer(self.BONUSCOIN, 0)
            pygame.time.set_timer(self.BONUSCOIN_CLEAR, 0)
            pygame.time.set_timer(self.BONUSCOIN, self.bonus_interval)
            
        # Обновление позиции персонажа
        # Получение координат мышки
        mouse_pos = pygame.mouse.get_pos()
        self.player.update(mouse_pos)
        return True

    def draw(self, screen):
        # отрисовка счета
        # Установка фона
        screen.fill(self.COLOR_FILL)
        
        score_font = pygame.font.SysFont('any_font', 36)
        str_score = f'Score: {self.score} Speed: {self.coin_countdown}ms' 
        score_block = score_font.render(str_score, False, (0, 0, 0))
        screen.blit(score_block,(150, HEIGHT-150))

        for coin in self.coin_list:
            # Отрисовка монеты
            screen.blit(coin.surf, coin.rect)

        for deadCoin in self.deadcoin_list:
            # Отрисовка dead-монеты
            screen.blit(deadCoin.surf, deadCoin.rect)
            
        for bonusCoin in self.bonus_list:
            # Отрисовка bonus-монеты
            screen.blit(bonusCoin.surf, bonusCoin.rect)
        
        # Отрисовка персонажа
        screen.blit(self.player.surf, self.player.rect)