#importar
import pygame
import random
import time
import sys
import ctypes

#importar variáveis de cor
White = (255,255,255)
Black = (0,0,0)
Green = (0,192,0)
LightGreen = (96,255,128)
Blue = (0,32,255)
Red = (255,0,0)
Grey = (105,105,105)

#Importar sons
pygame.mixer.init()
Button_Sound = pygame.mixer.Sound("Sons/Button.wav")
Music = pygame.mixer.music.load("Sons/Game Music.mp3")

#inicializar pygame
pygame.init()

class ecra:
    def __init__(self,width,height,caption):
        if(width<720):
            self.width=int(width)
            self.height=int(width+50)
        else: 
            self.width=720
            if (height<770):
                self.height=int(height)
                self.width=int(height-50)
            else:
                self.height=770
        self.center=int(self.width/2),int(self.height/2)
        pygame.display.set_caption(caption)
        self.caption=caption
        self.window= pygame.display.set_mode((self.width,self.height))

    def wipe(self):
        self.window.fill(Black)
    
    def update(self):
        pygame.display.update()

#get image screen
user32 = ctypes.windll.user32
screen=ecra(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1),"Super Tic-Tac-Toe")


        



def text(words, center, size,  color):
    """
    Parameters:
    words : string
    center : tuple (coords) or align
    size : integer
    color : name of color (from var "COLORS")
    """
    font = pygame.font.SysFont(None, size)
    text = font.render(words, True, color, None)
    textRect = text.get_rect()
    if center == "topleft":
        textRect.topleft = (10,10)
    elif center == "topmid":
        textRect.center = (int(screen.width/2),int(10+textRect.height/2))
    elif center == "bottomleft":
        textRect.bottomleft = (10,int(screen.height-10))
    elif center == "bottomright":
        textRect.bottomright = (int(screen.width-10),int(screen.height-10))
    elif center == "midbottom":
        textRect.midbottom = (int(screen.width/2),int(screen.height-10))
    elif center == "mid":
        textRect.center = screen.center
    else:
        textRect.center = center
    screen.window.blit(text, textRect)
    return textRect


def game_engine(mode,instruction):
    FramesPerSecond=30
    fpsclock=pygame.time.Clock()



    #rebuild
    screen.wipe()
    if not instruction:
        first_move=True
        gridmainfirst = pygame.image.load("Imagens/Grids/grid main1.png")
        grid_small = pygame.image.load("Imagens/Grids/grid small.png")

        screen.window.blit(gridmainfirst,(10,10))
        for i in [10,243+10,243*2+1]:
            for a in [10,243+10,243*2+1]:
                screen.window.blit(grid_small,(i,a))



    click=False
    while True:



        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.update()
        fpsclock.tick(FramesPerSecond)



def instruction_menu(comefromgame):

    def instructions(local,comefromgame):
        prev = False
        nxt = True
        screen.wipe()
        a = 0
        if local == 0:
            local = "Instruçoes/0Game and Logic/0_"
            max_a = 3
        elif local == 1:
            local = "Instruçoes/1Connection and Moves/1_"
            max_a = 4
        elif local ==2:
            local = "Instruçoes/2Points/2_"
            max_a = 1
        run1 = True
        while run1:
            page = pygame.image.load(f"{local}{a}.png").convert()
            screen.window.blit(page,(0,0))
            go_backRect = text("Return","topleft",30,(255,0,0))
            pygame.draw.rect(screen.window,(0,0,0),go_backRect)
            go_backRect = text("Return","topleft",30,(255,0,0))
            if a != 0:
                prev = True
                previousRect = text("<-- Previous","bottomleft",30,(255,255,255))
            if a < max_a:
                nextRect = text("Next -->","bottomright",30,(255,255,255))
            else:
                nxt = False
            screen.update()
            run = True
            click = False
            while run:
                mx,my = pygame.mouse.get_pos()
                if click:
                    if go_backRect.collidepoint((mx,my)):
                        Button_Sound.play()
                        if comefromgame:
                            instruction_menu(True)
                        else:
                            instruction_menu(False)
                    if prev and previousRect.collidepoint((mx,my)):
                        Button_Sound.play()
                        a -= 1
                        run = False
                    if nxt and nextRect.collidepoint((mx,my)):
                        Button_Sound.play()
                        a += 1
                        run = False
                click = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run1 = False
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True


    screen.wipe()
    game_and_logicRect = text("Game Map and Logic",(int(360/720*screen.width),int(190/770*screen.height)),40,(255,255,255))
    connection_and_movesRect = text("Connection and Moves",(360/720*screen.width,380/770*screen.height),40,(255,255,255))
    pointsRect = text("Points",(360/720*screen.width,570/770*screen.height),40,(255,255,255))
    go_backRect = text("Return","topleft",30,(255,0,0))
    screen.update()
    click = False
    run = True
    while run:
        #get mouse pos
        mx,my = pygame.mouse.get_pos()
        #butoes
        if click:
            if go_backRect.collidepoint((mx,my)):
                Button_Sound.play()
                if comefromgame:
                    print(1) #####
                    #game(False)
                else:
                    menu_inicial()
            if game_and_logicRect.collidepoint((mx,my)):
                Button_Sound.play()
                instructions(0,comefromgame)
            if connection_and_movesRect.collidepoint((mx,my)):
                Button_Sound.play()
                instructions(1,comefromgame)
            if pointsRect.collidepoint((mx,my)):
                Button_Sound.play()
                instructions(2,comefromgame)

        click = False
        #eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


def menu_inicial():

    def mode():
        screen.wipe()
        singlerect=text("Single-Player",(int(screen.width/2),int(screen.height/3)),70,White)
        multirect=text("Multi-Player",(int(screen.width/2),int(screen.height/3)*2),70,White)
        returnrect=text("Return","bottomleft",40,Red)
        screen.update()

        click=False
        while True:
            mx,my = pygame.mouse.get_pos()
            
            if click:
                if singlerect.collidepoint((mx, my)):
                    Button_Sound.play()
                    game_engine("single",False)
                if multirect.collidepoint((mx,my)):
                    Button_Sound.play()
                    game_engine("multi",False)
                if returnrect.collidepoint((mx,my)):
                    Button_Sound.play()
                    menu_inicial()

            click=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

    def load_gif_inicial(gif_Inicial,i):
        image = pygame.image.load(f"Imagens/GifInicial/{i}.jpg").convert()
        image = pygame.transform.scale(image, (int(300/720*screen.width), int(321/770*screen.height)))
        gif_Inicial.append(image)

        return gif_Inicial

    first_cycle=True
    gif_Inicial = []
    #gif instruments (framerate and current time)
    framerate_gif_Inicial = 0.06
    c_t_gif_Inicial = time.time()
    frame_gif_Inicial = 0

    #x and o animation
    phrase_animation = "X"
    coords_animation = (int(160/720*screen.width), int(478/770*screen.height))

    framerate_animation = 0.15
    c_t_animation = time.time()

    pygame.mixer.music.play(-1) #initialize music
    click = False
    #Draw
    screen.wipe()
    text("Super Tic Tac Toe",(int(360/720*screen.width),int(450/770*screen.height)),70,White)
    

    #PLAY BUTTON
    playRect = text("Play",(int(360/720*screen.width),int(520/770*screen.height)),40,(0,197,144))

    #instructions
    instructionRect = text("Instructions",(int(360/720*screen.width),int(560/770*screen.height)),40,(255,0,0))

    #obter imagem
    screen.update()
    
    run = True
    #Loop
    while run:
        #check mouse positions
        mx, my = pygame.mouse.get_pos()

        #x_and_o
        font = pygame.font.SysFont(None, 18)
        text_phrase_animation = font.render(phrase_animation, True, (180, 180, 180), None)
        screen.window.blit(text_phrase_animation, coords_animation)
        
        if time.time() > c_t_animation:
            phrase_animation += "   O" if phrase_animation[-1] == "X" else "   X"
            if len(phrase_animation) > 90:
                pygame.draw.rect(screen.window,(0, 0, 0),(160,478,720,25))
                phrase_animation = "X"
            c_t_animation += framerate_animation
            
        #gif
        if time.time() > c_t_gif_Inicial:
            frame_gif_Inicial = (frame_gif_Inicial) % 93
            if frame_gif_Inicial != 92 and first_cycle:
                gif_Inicial = load_gif_inicial(gif_Inicial,frame_gif_Inicial)
            else:
                if first_cycle:
                    gif_Inicial = load_gif_inicial(gif_Inicial,frame_gif_Inicial)
                first_cycle=False
            screen.window.blit(gif_Inicial[frame_gif_Inicial], (int(200/720*screen.width), int(55/770*screen.height)))
            frame_gif_Inicial += 1
            #obter imagem
            c_t_gif_Inicial += framerate_gif_Inicial
            pygame.display.update()
       #Check posições
        if click:
            if playRect.collidepoint((mx,my)):
                Button_Sound.play()
                gif_Inicial.clear()
                mode()
                
            if instructionRect.collidepoint((mx,my)):
                Button_Sound.play()
                gif_Inicial.clear()
                instruction_menu(False)
        click = False
        ##Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

if __name__ == "__main__":
    menu_inicial()