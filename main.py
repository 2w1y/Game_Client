#Config developer
ignore_serwer = True #jeśli true ignoruje połączenie z serwerem

#config weeb socket
import socket
import time
import pickle


PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.165"
ADDR = (SERVER, PORT)




### Config py game
import pygame, sys
 
mainClock = pygame.time.Clock()
from pygame.locals import *
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except:
    print("[Error]Serwer nie odpowiada może go odpal ty dzbanie")
    if ignore_serwer == True:
        pass
    else:
        sys.exit()

#starting options
pygame.init()
pygame.display.set_caption('game base')
WIDTH = 1920
HEIGHT = 1080
screensizex, screensizey = WIDTH,HEIGHT  # mniejszy ekran 1280 x 720 większy 1920 x 1080

SQ_SIZE = 45 #Od czego jest zależna ta zmienna ??
screen = pygame.display.set_mode((screensizex, screensizey),0,32)
 
font = pygame.font.SysFont(None, 20)
font_text = pygame.font.SysFont(None, 50)


#sending requests 
def send(msg):
    client.send(pickle.dumps(msg))
    print(f"[{client.recv(2048).decode(FORMAT)}] ")



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

def welcom_menu():
    running = True
    while running:
 
        screen.fill((27,72,171))
        draw_text('Główne menu', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1w = 250
        button_1 = pygame.Rect((screensizex/2) - (button_1w/2), screensizey/2 - 100, button_1w, 75)
        
        
        
        button_2 = pygame.Rect((screensizex/2) - (button_1w/2), screensizey/2 + 200, button_1w, 75)
        

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        
        pygame.draw.rect(screen, pygame.Color('lightskyblue3'), button_1)
        pygame.draw.rect(screen, pygame.Color('lightskyblue3'), button_2)
        
        button_1_text = font_text.render("Game",True,(255,255,255))
        screen.blit(button_1_text,(button_1.x + 5,button_1.y + 5))

        
        button_2_text = font_text.render("Ustawienia",True,(255,255,255))
        screen.blit(button_2_text,(button_2.x + 5,button_2.y + 5))

        #Draww logo
        image = pygame.image.load('logo.png')
        screen.blit(image, (0, HEIGHT-350))


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
        screen.fill((27,72,171))
        draw_text('Gra', font, (255, 255, 255), screen, 20, 20)
        
        
        GREY = (40, 50, 70)
        WHITE = (255, 255, 255)
        # drawing grids
        def draw_grid(a=0, b=0):
            for i in range(100):
                x = a + i % 10 * SQ_SIZE
                y = b + i // 10 * SQ_SIZE
                square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(screen, WHITE, square, width=1)
  
  
        #screen.fill(GREY)
        draw_grid(a=100, b=100)
        draw_grid(a=WIDTH - 100 - SQ_SIZE*10, b=100)
        
        #Draww logo
        image = pygame.image.load('logo.png')
        screen.blit(image, (0, HEIGHT-350))
        
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
        screen.fill((27,72,171))


        #Draww logo
        image = pygame.image.load('logo.png')
        screen.blit(image, (0, HEIGHT-350))

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



def register_menu():
    #dodać opcje iż podczas naciskania enter/tab przełącza na drugiego boxa do pisania
    input_login = ''
    input_password = ''
    symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    #color used
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    #buttons
    input_rect_login= pygame.Rect(200,200,140,45)
    
    input_rect_password= pygame.Rect(200,300,140,45)
    login_button= pygame.Rect(200,390,250,45)
    #params
    active_login = False
    active_password = False
    error_register = 0
    
    

    running = True
    while running:
        screen.fill((27,72,171))
        draw_text('register', font, (255, 255, 255), screen, 20, 20)
        
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


        draw_text('LOGIN: (Register)', font, (255, 255, 255), screen, input_rect_login.x, input_rect_login.y - 20)
        draw_text('PASSWORD:', font, (255, 255, 255), screen, input_rect_password.x, input_rect_password.y - 20)

        #login Button
        pygame.draw.rect(screen,color_active,login_button)
        text_surface_button_login = font_text.render("LOGIN",True,(255,255,255))
        screen.blit(text_surface_button_login,(login_button.x + 5,login_button.y + 5))

        #Error login
        if error_register == 1:
            draw_text('Nieprowawna nazwa lub hasło', font, (255, 0, 0), screen, input_rect_login.x, input_rect_login.y - 40)
        if error_register == 2:
            draw_text('Za którki login', font, (255, 0, 0), screen, input_rect_login.x, input_rect_login.y - 40)
        if error_register == 3:
            draw_text('Za którkie hasło', font, (255, 0, 0), screen, input_rect_password.x, input_rect_password.y - 40)


        #Draww logo
        image = pygame.image.load('logo.png')
        screen.blit(image, (0, HEIGHT-350))


        for event in pygame.event.get():
            if event.type == QUIT:
                send({"acctiviti":DISCONNECT_MESSAGE})
                pygame.quit()
                sys.exit()
            #inputs on/off
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

                #login backend
                if login_button.collidepoint(event.pos):
                    if len(input_login) >= 6:
                        if len(input_password) >= 6:
                            if ignore_serwer:
                                print("[Developer] Ignorwanie serwera jest włączone")
                                welcom_menu()
                                pass
                            else:
                                client.send(pickle.dumps({"acctiviti":"REGISTER","login":input_login,"password":input_password}))
                                if client.recv(2048).decode(FORMAT) == "True":
                                    print("Konto Utworzone")
                                    login_menu()
                                else:
                                    error_register = 1
                                    print("Nie udało Utworzyć konta")
                        else:
                            error_register = 3
                    else:
                        error_register = 2
            #navigation input
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

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
                                    print("Za długie hasło") #Tu będzie wyskawiać że za długie hasło
        

        pygame.display.update()
        mainClock.tick(60)


def login_menu():
    #dodać opcje iż podczas naciskania enter/tab przełącza na drugiego boxa do pisania
    input_login = ''
    input_password = ''
    symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    #color used
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    #buttons
    input_rect_login= pygame.Rect(200,200,140,45)
    
    input_rect_password= pygame.Rect(200,300,140,45)
    login_button= pygame.Rect(200,390,250,45)
    register_button = pygame.Rect(200,490,250,45)
    #params
    active_login = False
    active_password = False
    error_login = 0
    
    


    while True:
        screen.fill((27,72,171))
        draw_text('logowanie', font, (255, 255, 255), screen, 20, 20)
        #draw_text('enter na klawiaturze numerycznej aby przejść dalej', font, (255, 255, 255), screen, 1500, 980)
        
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


        draw_text('LOGIN:', font, (255, 255, 255), screen, input_rect_login.x, input_rect_login.y - 20)
        draw_text('PASSWORD:', font, (255, 255, 255), screen, input_rect_password.x, input_rect_password.y - 20)

        #login Button
        pygame.draw.rect(screen,color_active,login_button)
        text_surface_button_login = font_text.render("LOGIN",True,(255,255,255))
        screen.blit(text_surface_button_login,(login_button.x + 5,login_button.y + 5))

        #register Button
        pygame.draw.rect(screen,color_active,register_button)
        text_surface_button_register = font_text.render("Register",True,(255,255,255))
        screen.blit(text_surface_button_register,(register_button.x + 5,register_button.y + 5))

        #Error login
        if error_login == 1:
            draw_text('Nieprowawna nazwa lub hasło', font, (255, 0, 0), screen, input_rect_login.x, input_rect_login.y - 40)
        if error_login == 2:
            draw_text('Za którki login', font, (255, 0, 0), screen, input_rect_login.x, input_rect_login.y - 40)
        if error_login == 3:
            draw_text('Za którkie hasło', font, (255, 0, 0), screen, input_rect_password.x, input_rect_password.y - 40)


        #Draww logo
        image = pygame.image.load('logo.png')
        screen.blit(image, (0, HEIGHT-350))



        for event in pygame.event.get():
            if event.type == QUIT:
                send({"acctiviti":DISCONNECT_MESSAGE})
                pygame.quit()
                sys.exit()
            #inputs on/off
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
                #register backend
                if register_button.collidepoint(event.pos):
                    register_menu()

                #login backend
                if login_button.collidepoint(event.pos):
                    if len(input_login) >= 6:
                        if len(input_password) >= 6:
                            if ignore_serwer:
                                print("[Developer] Ignorwanie serwera jest włączone")
                                welcom_menu()
                                pass
                            else:
                                client.send(pickle.dumps({"acctiviti":"LOGIN","login":input_login,"password":input_password}))
                                if client.recv(2048).decode(FORMAT) == "True":
                                    print("zalogowano")
                                    welcom_menu()
                                else:
                                    error_login = 1
                                    print("Nie udało się zalogować ")
                        else:
                            error_login = 3
                    else:
                        error_login = 2
            #navigation input
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    send({"acctiviti":DISCONNECT_MESSAGE})
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
