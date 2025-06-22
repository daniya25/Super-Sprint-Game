import pygame
import random 
import time
pygame.init()#need to initialise pygame in order to use its features.


#time module
clock=pygame.time.Clock()

#colour values

green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

#the screen size and caption 
width=800
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Racing")

#paused function

def paused():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruction_background,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",80)
        textsurface,textrect=text_objects("PAUSED",largetext)
        textrect.center=((400),(150))
        screen.blit(textsurface,textrect)
#for continue
        pygame.draw.rect(screen,(0,0,0),(70,230,240,50))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if mouse[0]>70 and mouse[0]<310 and mouse[1]>230 and mouse[1]<290:
            pygame.draw.rect(screen,(245,245,220),(70,230,240,50))
            if click==(1,0,0):
                paused=False
                
        smalltext=pygame.font.Font("freesansbold.ttf",40)
        textsurface,textrect=text_objects("CONTINUE",smalltext)
        textrect.center=(70+(230/2)),(230+(50/2))
        screen.blit(textsurface,textrect)
#for restart
        pygame.draw.rect(screen,(0,0,0),(70,330,240,50))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if mouse[0]>70 and mouse[0]<310 and mouse[1]>330 and mouse[1]<380:
            pygame.draw.rect(screen,(245,245,220),(70,330,240,50))
            if click==(1,0,0):
                game_loop()
        smalltext=pygame.font.Font("freesansbold.ttf",40)
        textsurface,textrect=text_objects("RESTART",smalltext)
        textrect.center=(70+(240/2)),(330+(50/2))
        screen.blit(textsurface,textrect)
#for main menu
        pygame.draw.rect(screen,(0,0,0),(70,430,240,50))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if mouse[0]>70 and mouse[0]<310 and mouse[1]>430 and mouse[1]<480:
            pygame.draw.rect(screen,(245,245,220),(70,430,240,50))
            if click==(1,0,0):
                intro_loop()
        
        smalltext=pygame.font.Font("freesansbold.ttf",40)
        textsurface,textrect=text_objects("MAIN MENU",smalltext)
        textrect.center=(70+(240/2)),(430+(50/2))
        screen.blit(textsurface,textrect)
        pygame.display.update()
        clock.tick(5)


#instruction function

def instruction():
    instruction=True
    while instruction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruction_background,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",80)
        mediumtext=pygame.font.Font("freesansbold.ttf",40)
        smalltext=pygame.font.Font("freesansbold.ttf",20)
        textsurface,textrect=text_objects("INSTRUCTION",largetext)
        textrect.center=((400,100))
        screen.blit(textsurface,textrect)
        textsurface1,textrect1=text_objects("",smalltext)
        textrect1.center=((290,200))
        screen.blit(textsurface1,textrect1)
        textsurface2,textrect2=text_objects("<-: LEFT DISPLACEMENT",smalltext)
        textrect2.center=((170,300))
        screen.blit(textsurface2,textrect2)
        textsurface3,textrect3=text_objects("->: RIGHT DISPLACEMENT",smalltext)
        textrect3.center=((170,400))
        screen.blit(textsurface3,textrect3)
        textsurface4,textrect4=text_objects("Dont exceed the road boundary",smalltext)
        textrect4.center=((150,480))
        screen.blit(textsurface4,textrect4)
        textsurface5,textrect5=text_objects("Get Set Go!",smalltext)
        textrect5.center=((150,560))
        screen.blit(textsurface5,textrect5)
        pygame.draw.rect(screen,(0,0,0),(640,400,150,50))            
        mouse=pygame.mouse.get_pos()
        if mouse[0]>640 and mouse[0]<790 and mouse[1]>400 and mouse[1]<450:
            pygame.draw.rect(screen,(245,245,220),(640,400,150,50))
        smalltext=pygame.font.Font("freesansbold.ttf",30)
        textsurface,textrect=text_objects("BACK",smalltext)
        textrect.center=(640+(150/2)),(400+(50/2))
        screen.blit(textsurface,textrect)        
        click=pygame.mouse.get_pressed()
        if click==(1,0,0):
            intro_loop()        


        pygame.display.update()
        



#function for the obstacle
def obstacle(obs_x,obs_y,obs):
    if obs==0:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car3.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car7.jpg")
    screen.blit(obs_pic,(obs_x,obs_y))   
    

#loading the image
carimg=pygame.image.load('car1.jpg')
grass=pygame.image.load('grass.jpg')
yellow_strip=pygame.image.load('yellow_strip.jpg')
strip=pygame.image.load('strip.jpg')
intro_bg_=pygame.image.load("background4.jpg")
intro_image=pygame.transform.scale(intro_bg_,(950,700))
instruction_bg=pygame.image.load("background6.jpg")
instruction_background=pygame.transform.scale(instruction_bg,(950,700))

#tex_objects function

def text_objects(text,font):
    textsurface=font.render(text,True,(255,255,255))
    return textsurface,textsurface.get_rect()


#introloop

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        

        screen.blit(intro_image,(0,0))
        font=pygame.font.Font("freesansbold.ttf",70)
        title=font.render("CAR RACE GAME",1,(255,255,255))
        screen.blit(title,(90,50))
        pygame.draw.rect(screen,(0,0,0),(80,150,220,90))
        pygame.draw.rect(screen,(0,0,0),(300,250,300,90))
        pygame.draw.rect(screen,(0,0,0),(560,150,220,90))
        mouse=pygame.mouse.get_pos()
        
        click=pygame.mouse.get_pressed()
        
        if mouse[0]>70 and mouse[0]<300 and mouse[1]>150 and mouse[1]<250:
            pygame.draw.rect(screen,(245,245,220),(80,150,220,90))
            if click==(1,0,0):
                countdown()
        if mouse[0]>300 and mouse[0]<640 and mouse[1]>250 and mouse[1]<340:
            pygame.draw.rect(screen,(245,245,220),(300,250,300,90))
            if click==(1,0,0):
                instruction()
        if mouse[0]>550 and mouse[0]<780 and mouse[1]>150 and mouse[1]<250:
            pygame.draw.rect(screen,(245,245,220),(560,150,220,90))
            if click==(1,0,0):
                pygame.quit()
                quit()
        smalltext=pygame.font.Font("freesansbold.ttf",30)
        textsurface,textrect=text_objects("START",smalltext)
        textrect.center=(80+(220/2)),(150+(90/2))
        screen.blit(textsurface,textrect)
        
        textsurface,textrect=text_objects("INSTRUCTIONS",smalltext)
        textrect.center=(300+(300/2)),(250+(90/2))
        screen.blit(textsurface,textrect)

        textsurface,textrect=text_objects("QUIT",smalltext)
        textrect.center=(560+(220/2)),(150+(90/2))
        screen.blit(textsurface,textrect)
        
        
        
        pygame.display.update()
#car width
car_width=56

#crashed message
myfont=pygame.font.Font("freesansbold.ttf",70)
render_text=myfont.render("CAR CRASHED!!",1,(0,0,0))



#function for adding the background images

def background():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(400,0))
    screen.blit(yellow_strip,(400,100))
    screen.blit(yellow_strip,(400,200))
    screen.blit(yellow_strip,(400,300))
    screen.blit(yellow_strip,(400,400))
    screen.blit(yellow_strip,(400,500))
    screen.blit(yellow_strip,(400,600))
    screen.blit(strip,(120,0))
    screen.blit(strip,(680,0))

#function score card
def score_card(car_passed,score):
    font=pygame.font.SysFont(None,35)
    passed=font.render("Passed: "+str(car_passed),True,(255,255,255))
    score=font.render("Score: "+str(score),True,(0,0,0))
    screen.blit(passed,(0,50))
    screen.blit(score,(0,100))

#image_appearing-blit
def car(x,y):
    screen.blit(carimg,(x,y))



def countdown_background():
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
    font=pygame.font.Font("freesansbold.ttf",35)
    x=(width*0.45)
    y=(height*0.8)
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(400,0))
    screen.blit(yellow_strip,(400,100))
    screen.blit(yellow_strip,(400,200))
    screen.blit(yellow_strip,(400,300))
    screen.blit(yellow_strip,(400,400))
    screen.blit(yellow_strip,(400,500))
    screen.blit(yellow_strip,(400,600))
    screen.blit(strip,(120,0))
    screen.blit(strip,(680,0))
    screen.blit(carimg,(x,y))
    passed=font.render("Passed:0",True,(255,255,255))
    score=font.render("Score:0",True,(0,0,0))
    screen.blit(passed,(0,50))
    screen.blit(score,(0,100))

#countdown function

def countdown():
    countdown=True
    while countdown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        
        screen.fill((119,118,110))
        countdown_background()
        largetext=pygame.font.SysFont(None,115)
        
        textsurface,textrect=text_objects("3",largetext)
        textrect.center=((width/2),(height/2))
        screen.blit(textsurface,textrect)
        pygame.display.update()
        clock.tick(1)
        
        screen.fill((119,118,110))
        countdown_background()
        largetext=pygame.font.SysFont(None,115)
        
        textsurface,textrect=text_objects("2",largetext)
        textrect.center=((width/2),(height/2))
        screen.blit(textsurface,textrect)
        pygame.display.update()
        clock.tick(1)
        
        screen.fill((119,118,110))
        countdown_background()
        largetext=pygame.font.SysFont(None,115)
       
        textsurface,textrect=text_objects("1",largetext)
        textrect.center=((width/2),(height/2))
        screen.blit(textsurface,textrect)
        pygame.display.update()
        clock.tick(1)
        
        screen.fill((119,118,110))
        countdown_background()
        largetext=pygame.font.Font("freesansbold.ttf",115)
        
        textsurface,textrect=text_objects("GO!!!",largetext)
        textrect.center=((width/2),(height/2))
        screen.blit(textsurface,textrect)
        pygame.display.update()
        clock.tick(1)

        game_loop()

        





#game loop
def game_loop():
    bumped=False
    x_change=0
    x=400
    y=470
    obstacle_speed=10
    obs=0
    y_change=0
    obs_x=random.randrange(200,650)
    obs_y=-750   
    enemy_width=56
    enemy_height=125
    car_passed=0
    score=0
    level=0
    

       

    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
             
              
        
        #moving x,y coordinates
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_s:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
       
        x+=x_change
           
        #print("benzooo")
        #background colour
        screen.fill((119,119,119))
        background()
        obs_y-=(obstacle_speed/4)
        obstacle(obs_x,obs_y,obs)
        obs_y+=obstacle_speed
        
        #calling the car function
        car(x,y)
        
        #calling the score function

        score_card(car_passed,score)
      
        if x>680-car_width or x<120:
           screen.blit(render_text,(120,180))
           pygame.display.update()
           time.sleep(5)
           game_loop()


        #for the enemy car to keep coming back after it leaves the screen

        if obs_y>height:
            obs_y=0-enemy_height
            obs_x=random.randrange(170,width-170)
            obs=random.randrange(0,6)
            car_passed+=1
            score=car_passed*10
            if int(car_passed)%10==0:
                level+=1
                obstacle_speed+=2
                myfont=pygame.font.SysFont(None,100)
                level_text=myfont.render("Level"+str(level),1,(0,0,0))
                screen.blit(level_text,(100,200))
                pygame.display.update()
                time.sleep(3)


        #right side and left side gaadi crashing

        if y<obs_y+enemy_height:
            if x>obs_x and x<obs_x+enemy_width or x+car_width>obs_x and x+car_width<obs_x+enemy_width:
                screen.blit(render_text,(120,180))
                pygame.display.update()
                time.sleep(5)
                game_loop()
     
        pygame.draw.rect(screen,(0,0,0),(650,0,150,70))
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if mouse[0]>650 and mouse[0]<800 and mouse[1]>0 and mouse[1]<50:
            pygame.draw.rect(screen,(255,255,255),(650,0,150,70))
            if click==(1,0,0):
                paused()
        smalltext=pygame.font.Font("freesansbold.ttf",30)
        textsurface,textrect=text_objects("PAUSE",smalltext)
        textrect.center=(650+(150/2)),(0+(70/2))
        screen.blit(textsurface,textrect)         
   
        
            
        
        
        #updating the screen
        pygame.display.update()
        clock.tick(90) 
 
intro_loop()
game_loop()
pygame.quit()
quit()
