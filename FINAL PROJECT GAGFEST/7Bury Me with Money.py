import pygame
import random


pygame.init()

pygame.mixer.init()

collision_sound = pygame.mixer.Sound('voice.wav')  

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h 


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bury me with money')

coin_image = pygame.image.load('Coin.png')  
coin_image = pygame.transform.scale(coin_image, 
                                    (coin_image.get_width() // 2, coin_image.get_height() // 2)) 

coin_width, coin_height = coin_image.get_size()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - coin_width)  
        self.rect.y = -coin_height 
        self.speed = random.randint(4, 10) 

    def update(self):

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:  
            self.rect.y = -coin_height 
            self.rect.x = random.randint(0, WIDTH - coin_width)  


all_coins = pygame.sprite.Group()


basket_image = pygame.image.load('Basket.png') 
basket_image = pygame.transform.scale(basket_image, 
                                      (basket_image.get_width() * 2 // 10, basket_image.get_height() * 2 // 10))  # 缩小篮子图像
basket_width, basket_height = basket_image.get_size()
basket_rect = basket_image.get_rect()

basket_rect.y = HEIGHT - basket_height

score = 0
font = pygame.font.Font(None, 36) 
score_font = pygame.font.Font(None, 36)  
message_font = pygame.font.Font(None, 72)  
button_font = pygame.font.Font(None, 48)  

class Button:
    def __init__(self, x, y, width, height, text, font, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_surface = font.render(text, True, (255, 255, 255)) 

    def draw(self, screen):
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=20)  
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=20) 
        
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def is_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_x, mouse_y) and mouse_pressed[0]:
            return True
        return False


start_again_button = Button(WIDTH // 2 - 150, HEIGHT // 2 + 100, 300, 60, 'Start Again', button_font, (255, 133, 17), (255, 90, 17))

running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    
    basket_rect.x = mouse_x - basket_width // 2  
    if basket_rect.x < 0: 
        basket_rect.x = 0
    elif basket_rect.x > WIDTH - basket_width:  
        basket_rect.x = WIDTH - basket_width

    
    if len(all_coins) < 10: 
        coin = Coin()
        all_coins.add(coin)

   
    all_coins.update()

    
    for coin in all_coins:
        if coin.rect.colliderect(basket_rect): 
            coin.kill()  
            score += 1  
            collision_sound.play()  

    
    screen.fill((172, 213, 152)) 

    
    all_coins.draw(screen)


    screen.blit(basket_image, basket_rect)

    
    score_text = score_font.render("Score", True, (255, 112, 17)) 
    score_value_text = score_font.render(str(score), True, (255, 112, 17)) 

    
    total_width = score_text.get_width() + score_value_text.get_width() + 20  
    box_width = total_width + 40 
    box_height = max(score_text.get_height(), score_value_text.get_height()) + 20  
    box_x = (WIDTH - box_width) // 2 
    box_y = 10  

    
    pygame.draw.rect(screen, (255, 255, 255, 204), pygame.Rect(box_x, box_y, box_width, box_height), border_radius=20)  # 圆角框

    
    screen.blit(score_text, (box_x + 10, box_y + (box_height - score_text.get_height()) // 2))
    screen.blit(score_value_text, (box_x + score_text.get_width() + 20, box_y + (box_height - score_value_text.get_height()) // 2))

   
    if score >= 50:
        
        message_text = message_font.render("Yeah! You have been buried with money!", True, (255, 112, 17))  
        message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        
        box_width = message_rect.width + 40
        box_height = message_rect.height + 40
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)  
        box_surface.fill((255, 255, 255, 204),) 

        pygame.draw.rect(box_surface, (255, 255, 255, 204), pygame.Rect(0, 0, box_width, box_height), border_radius=20)

        screen.blit(box_surface, (message_rect.x - 20, message_rect.y - 20))  
        screen.blit(message_text, message_rect) 

        start_again_button.draw(screen)

        if start_again_button.is_clicked():
            score = 0
            all_coins.empty() 

    pygame.display.flip()

    clock.tick(90)

pygame.quit()
