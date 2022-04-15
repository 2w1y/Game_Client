
import pygame, sys
 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screensizex, screensizey = 1920, 1080
screen = pygame.display.set_mode((screensizex, screensizey),0,32)
 
font = pygame.font.SysFont(None, 20)
font_text = pygame.font.SysFont(None, 50)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def welcom_menu():
    running = True
    while running:
 
        screen.fill((0,0,0))
        draw_text('Główne menu', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1w = 250
        button_1 = pygame.Rect((screensizex/2) - (button_1w/2), screensizey/2 - 100, button_1w, 75)
        button_2 = pygame.Rect((screensizex/2) - (button_1w/2), screensizey/2 + 200, button_1w, 75)
        #print(button_1.width)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        text = ''
        pygame.draw.rect(screen, (255, 255, 255), button_1)
        pygame.draw.rect(screen, (255, 255, 255), button_2)
        draw_text(text, font, (255, 0, 0), screen, 50, 100)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Gra', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Elo Elo 320 Opcje tu są grane zero', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def login_menu():
    input_login = ''
    input_password = ''
    symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    color = color_passive
    
    input_rect_login= pygame.Rect(200,200,140,45)
    input_rect_password= pygame.Rect(200,300,140,45)
    active_login = False
    active_password = False
    while True:
        screen.fill((0,0,0))
        draw_text('logowanie', font, (255, 255, 255), screen, 20, 20)
        draw_text('enter na klawiaturze numerycznej aby przejść dalej', font, (255, 255, 255), screen, 1500, 980)
        
        #user input login
        if active_login:
            color_login = color_active
            box_login = 3
        else:
            color_login = color_passive
            box_login = 2
        
        #user input password
        if active_password:
            color_password = color_active
            box_password = 3
        else:
            color_password = color_passive
            box_password = 2



        #Login box
        pygame.draw.rect(screen,color_login,input_rect_login,box_login)
        text_surface_login = font_text.render(input_login,True,(255,255,255))
        screen.blit(text_surface_login,(input_rect_login.x + 5,input_rect_login.y + 5))
        input_rect_login.w = max(250, text_surface_login.get_width()+ 10)
        
        #Password box
        pygame.draw.rect(screen,color_password,input_rect_password,box_password)
        text_surface_password = font_text.render("*" * len(input_password),True,(255,255,255))
        screen.blit(text_surface_password,(input_rect_password.x + 5,input_rect_password.y + 5))
        input_rect_password.w = max(250, text_surface_password.get_width()+ 10)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_login.collidepoint(event.pos):
                    active_login = True
                    active_password = False
                elif input_rect_password.collidepoint(event.pos):
                    active_password = True
                    active_login = False
                else:
                    active_login = False
                    active_password = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_KP_ENTER:
                    welcom_menu()

                #login input
                if active_login:
                    if event.key == K_BACKSPACE:
                        input_login = input_login[:-1]
                    else:
                        for symbol in symbols:
                            if symbol == event.unicode.casefold():
                                if len(input_login) != 20:
                                    input_login += event.unicode
                                else:
                                    print("Za długi login") #Tu będzie wyskawiać że za długi logi

                #password input
                if active_password:
                    if event.key == K_BACKSPACE:
                        input_password = input_password[:-1]
                    else:
                        for symbol in symbols:
                            if symbol == event.unicode.casefold():
                                if len(input_password) != 20:
                                    input_password += event.unicode
                                else:
                                    print("Za długi hasło") #Tu będzie wyskawiać że za długie hasło
        
        pygame.display.update()
        mainClock.tick(60)


login_menu()