
import pygame as py

#   SCREEN CLASS FOR WINDOW HAVING THE FUCNTION OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN
class Screen():
    
    #   INITIALIZATION OF WINDOW HAVING TITLE, WIDTH, HEIGHT AND COLOUR 
    def __init__(self,title,width=440,height=445,fill=(0,0,255)):   # HERE (0,0,255) IS A COLOUR CODE
        self.height = height    #   HEIGHT OF A WINDOW
        self.title = title      #   TITLE OF A WINDOW
        self.width = width      #   WIDTH OF A WINDOW
        self.fill = fill        #   COLOUR CODE
        self.CurrentState= False #   CURRENT STATE OF A SCREEN
    
    #   DISPLAY THE CURRENT SCREEN OF A WINDOW AT THE CURRENT STATE
    def makeCurrentScreen(self):
        py.display.set_caption(self.title)  #   SET THE TITLE FOR THE CURRENT STATE OF A SCREEN
        self.CurrentState = True     #   SET THE STATE TO ACTIVE
        self.screen=py.display.set_mode((self.width,self.height))   #   ACTIVE SCREEN SIZE
    

    #   THIS WILL SET THE STATE OF A CURRENT STATE TO OFF
    def endCurrentScreen(self):
        self.CurrentState = False
    
    #   THIS WILL CONFIRM WHEHTER THE NAVIGATION OCCURS
    def checkUpdate(self,fill):
        self.fill=fill  #   HERE FILL IS THE COLOR CODE
        return self.CurrentState    

    #   THIS WILL UPDATE THE SCREEN WITH THE NEW NAVIGATION TAB
    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.fill)
    
    #   RETURNS THE TITLE OF THE SCREEN
    def returnTitle(self):
        return self.screen

#   NAVIGATION BUTTON CLASS
class Button():

    #   INITIALIZATION OF BUTTON COMPONENTS LIKE POSITION OF BUTTON, COLOR OF BUTTON, FONT COLOR OF BUTTON, FONT SIZE, TEXT INSIDE THE BUTTON
    def __init__(self,x,y,sx,sy,bcolour,fbcolour,font,fcolour,text):
        self.x = x  #   ORIGIN_X COORDINATE OF BUTTON
        self.y = y  #   ORIGIN_Y COORDINATE OF BUTTON
        self.sx = sx #  LAST_X COORDINATE OF BUTTON
        self.sy = sy   #   LAST_Y COORDINATE OF BUTTON
        self.fontsize = 25  #   FONT SIZE FOR THE TEXT IN A BUTTON
        self.bcolour = bcolour  #   BUTTON COLOUR
        self.fbcolour = fbcolour    #   RECTANGLE COLOR USED TO DRAW THE BUTTON
        self.fcolour = fcolour      #   BUTTON FONT COLOR
        self.text = text    #   TEXT IN A BUTTON
        self.CurrentState = False   #   CURRENT IS OFF
        self.buttonf = py.font.SysFont(font,self.fontsize)  #   FONT OBJECT FROM THE SYSTEM FONTS

    #   DRAW THE BUTTON FOR THE TWO TABS MENU_SCREEN AND CONTROL TABS MENU
    def showButton(self,display):
        if(self.CurrentState):
            py.draw.rect(display,self.fbcolour,(self.x,self.y,self.sx,self.sy))
        else:
            py.draw.rect(display,self.fbcolour,(self.x,self.y,self.sx,self.sy))

        textsurface=self.buttonf.render(self.text,False,self.fcolour)   #   RENDER THE FONT OBJECT FROM THE STSTEM FONTS
        
        #   THIS LINE WILL DRAW THE SURF ONTO THE SCREEN
        display.blit(textsurface,((self.x + (self.sx/2) - (self.fontsize/2)*(len(self.text)/2) - 5, (self.y + (self.sy/2) - (self.fontsize/2)-4) )))

    # THIS FUCNTION CAPTURE WHETHER ANY MOUSE EVENT OCCUR ON THE BUTTON
    def focusCheck(self,mousepos,mouseclick):
        if( mousepos[0] >= self.x and mousepos[0] <= self.x + self.sx and mousepos[1] >= self.y and mousepos[1] <= self.y + self.sy):
            self.CurrentState = True
            return mouseclick[0]    # IF MOUSE BUTTON CLICK THEN NAVIGATE TO THE NEXT OR PREVIOUS TABS
        
        else:
            self.CurrentState = False   # ELSE LET THE CURRENT STATE TO BE OFF
            return False

py.init()   # INITIALIZATION OF THE PYGAME

py.font.init()  # INITIALIZATION OF SYSTEM FONTS

menuScreen = Screen("Menu Screen")  #   CREATING THE OBJECT OF THE CLASS Screen FOR MENU SCREEN
control_bar= Screen("Control Screen")   #   CREATING THE OBJECT OF THE CLASS Screen FOR CONTROL SCREEN

win = menuScreen.makeCurrentScreen()    #  CALLING OF THE FUNCTION TO MAKE THE SCREEN FOR THE WINDOW

#  MENU BUTTON
MENU_BUTTON = Button(150,150,150,50, (255,250,250), (255,0,0), "TimesNewRoman", (255,255,255), "Main Menu")

#  CONTROL BUTTON
CONTROL_BUTTON = Button(150,150,150,50, (0,0,0), (0,0,255), "TimesNewRoman",  (255,255,255), "Back")

done = False

toggle = False

# MAIN LOOPING
while not done:
    menuScreen.screenUpdate()   #  CALLING OF screenUpdate function FOR MENU SCREEN
    control_bar.screenUpdate()  #  CALLING THE FUNCTION OF CONTROL BAR
    mouse_pos = py.mouse.get_pos()  #   STORING THE MOUSE EVENT TO CHECK THE POSITION OF THE MOUSE
    mouse_click = py.mouse.get_pressed()    #  CHECKING THE MOUSE CLICK EVENT
    keys = py.key.get_pressed() #  KEY PRESSED OR NOT

#   MENU BAR CODE TO ACCESS
    if menuScreen.checkUpdate((25,0,255)):  #  CHECKING MENU SCREEN FOR ITS UPDATE
        control_barbutton=MENU_BUTTON.focusCheck(mouse_pos, mouse_click)
        MENU_BUTTON.showButton(menuScreen.returnTitle())

        if control_barbutton:
            win = control_bar.makeCurrentScreen()
            menuScreen.endCurrentScreen()

#   CONTROL BAR CODE TO ACCESS
    elif control_bar.checkUpdate((255,0,255)):  #  CHECKING CONTROL SCREEN FOR ITS UPDATE
        return_back = CONTROL_BUTTON.focusCheck(mouse_pos, mouse_click)
        CONTROL_BUTTON.showButton(control_bar.returnTitle())

        if return_back:
            control_bar.endCurrentScreen()
            win = menuScreen.makeCurrentScreen()
    
    for event in py.event.get():    #  CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
        if(event.type == py.QUIT):  # IF CLICKED THEN CLOSE THE WINDOW
            done =True              
    
    py.display.update()            
py.quit()                       #  CLOSE THE PROGRAM 

