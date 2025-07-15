from quarternion_c2027453 import *
from facing_c2027453 import *
from render_c2027453 import *
from data_c2027453 import*
from quicksort_c2027453 import *
from eulerRotation_c2027453 import *
import pygame_gui
import sys
'''
Render Parameters
'''
Cube = data("3D_Models/Cube.txt")

White = (255,255,255)
Black = (0,0,0)
Blue = (0,0,255)
LightBlue = (100,100,255)
Grey = (160,160,160)
Green = (0,255,0)

zoffset = 10 #Moves The Z axis away from the camera by the offset

viewDistance = 5

Size = [1000, 700]

offset = [Size[0]/2, Size[1]/2]

pos = [0,0,0]

scale = 150

pygame.init()

clock = pygame.time.Clock()

scene=pygame.display.set_mode(Size)

UI = pygame_gui.UIManager(Size)

angle = 0.5

eulerAngle = [0,0,0]

increment = 0.01

axis=[1,1,1]

'''5
GUI Settings
'''
#GUI For Axis Settings
xaxis = pygame_gui.elements.UITextEntryLine(relative_rect=
                                            pygame.Rect((100,650),
                                                        (45,25))
                                                        ,manager=UI,object_id="#xaxis")

yaxis = pygame_gui.elements.UITextEntryLine(relative_rect=
                                            pygame.Rect((150,650),
                                                        (45,25))
                                                        ,manager=UI,object_id="#yaxis")

zaxis = pygame_gui.elements.UITextEntryLine(relative_rect=
                                            pygame.Rect((200,650),
                                                        (45,25))
                                                        ,manager=UI,object_id="#zaxis")

button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((100, 675),
                                                  (145,25)),text='Axis',
                                                  manager=UI,object_id="#AxisButton")

#GUI For Position Settings
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((425, 650),
                                                  (45,25)),text='+X',
                                                  manager=UI,object_id="#+XP")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((425, 675),
                                                  (45,25)),text='-X',
                                                  manager=UI,object_id="#-XP")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((475, 650),
                                                  (45,25)),text='+Y',
                                                  manager=UI,object_id="#+YP")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((475, 675),
                                                  (45,25)),text='-Y',
                                                  manager=UI,object_id="#-YP")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((525, 650),
                                                  (45,25)),text='+Z',
                                                  manager=UI,object_id="#+ZP")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((525, 675),
                                                  (45,25)),text='-Z',
                                                  manager=UI,object_id="#-ZP")

#GUI For Rotation Method Selection
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((100, 625),
                                                  (145,25)),text='Quarternion',
                                                  manager=UI,object_id="#Quarternion")

button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((800, 625),
                                                  (145,25)),text='Euler',
                                                  manager=UI,object_id="#Euler")

#GUI For Euler Angles
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((800, 650),
                                                  (45,25)),text='+X',
                                                  manager=UI,object_id="#+X")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((800, 675),
                                                  (45,25)),text='-X',
                                                  manager=UI,object_id="#-X")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((850, 650),
                                                  (45,25)),text='+Y',
                                                  manager=UI,object_id="#+Y")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((850, 675),
                                                  (45,25)),text='-Y',
                                                  manager=UI,object_id="#-Y")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((900, 650),
                                                  (45,25)),text='+Z',
                                                  manager=UI,object_id="#+Z")
button = pygame_gui.elements.UIButton(relative_rect=
                                      pygame.Rect((900, 675),
                                                  (45,25)),text='-Z',manager=UI,object_id='#-Z')
                                                

#Text GUI Settings For Drop Menu
modelRect = pygame.Rect((100, 575), (150, 25))
modelRect_text = pygame.Rect((250, 585), (250, 50))
dropdown = pygame_gui.elements.UIDropDownMenu(['Cube', 'Teapot', 'Maxwell'], 'Cube',
                                              pygame.Rect((100, 575), (150, 25)),
                                              manager=UI,object_id="#rotationType")

modelText = pygame.font.SysFont("bahnschrift",20).render(f"drop down menu to select\n3d model",True,"Black")

#Toggle x & y reflections
button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800,325),(145,25)),
                                                 text='Reflect x=0',
                                                  manager=UI,object_id="#XReflect")

button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800,350),(145,25)),
                                                 text='Reflect y=0',
                                                  manager=UI,object_id="#YReflect")

button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800,375),(145,25)),
                                                 text='Reflect z=0',
                                                  manager=UI,object_id="#ZReflect")
ReflectRect=pygame.Rect((800,325),(145,75))
ReflectRect_Text=pygame.Rect((655,350),(145,75))
ReflectText = pygame.font.SysFont("bahnschrift",20).render(f"Click to toggle\nreflection on\nspecified axis",True,"Black")
                                      
#Auto Rotate Button
spinRect = pygame.Rect((450, 0),(100,50))
spinRect_text = pygame.Rect((550, 0),(220,50))
button = button = pygame_gui.elements.UIButton(relative_rect=spinRect,
                                                 text='Auto Spin',
                                                  manager=UI,object_id="#Spin")

spinText = pygame.font.SysFont("bahnschrift",20).render(f"Click to toggle autospin",True,"Black") 

'''
Binary Variables
'''
euler = True

Spin = True

XReflect = False

YReflect = False

ZReflect = False

'''
Updates To Run Checks
'''
RenderCube=True
while RenderCube:
    '''
    GUI Checks
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Checks For Axis Settings
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#AxisButton":
            try:
                axis[0]=float(xaxis.get_text())
            except:
                print("Error: Please enter a valid x")
                axis[0]=0
            xaxis.set_text("")

            try:
                axis[1]=float(yaxis.get_text())
            except:
                print("Error: Please enter a valid y")
                axis[1]=0
            yaxis.set_text("")

            try:
                axis[2]=float(zaxis.get_text())
            except:
                print("Error: Please enter a valid z")
                axis[2]=0
            zaxis.set_text("")

        #Checks For Model Selection
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.text=="Cube":
                Cube=data("3D_Models/Cube.txt")
                scale=150
                print("Selected: Cube")

        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.text=="Teapot":
                Cube=data("3D_Models/TeapotData.txt")
                scale=200
                print("Selected: Teapot")
                
                
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.text=="Maxwell":
                Cube=data("3D_Models/maxwellData.txt")
                scale=100
                print("Selected: Maxwell")

        #Checks For Button Selection For Rotation Method Used
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#Quarternion":
            euler=False
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#Euler":
            euler=True

        #Checks For Euler Angles Buttons
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#+X":
            eulerAngle[0] += increment*5
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#-X":
            eulerAngle[0] -= increment*5

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#+Y":
            eulerAngle[1] += increment*5
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#-Y":
            eulerAngle[1] -= increment*5

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#+Z":
            eulerAngle[2] += increment*5
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#-Z":
            eulerAngle[2] -= increment*5

        #Checks For Position Buttons
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#+XP":
            pos[0] += 0.5
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#-XP":
            pos[0] -= 0.5

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#+YP":
            pos[1] -= 0.5
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#-YP":
            pos[1] += 0.5

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#+ZP":
            pos[2] -= 0.5
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#-ZP":
            pos[2] += 0.5

        #Checks For Position Settings
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#Pos":
            try:
                pos[0]=float(x.get_text())
            except:
                print("Error: Please enter a valid x")
                pos[0]=0
            x.set_text("")

            try:
                pos[1]=-float(y.get_text())
            except:
                print("Error: Please enter a valid y")
                pos[1]=0
            y.set_text("")

            try:
                pos[2]=float(z.get_text())
            except:
                print("Error: Please enter a valid z")
                pos[2]=10
            z.set_text("")

        #Toggle For AutoSpin Checks
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#Spin":
            print("Auto Spin Toggled On/Off")
            if Spin == True:
                Spin = False
            else:
                Spin = True

        #Toggle Reflection At Axis Specified
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#XReflect":
            print("Auto Spin Toggled On/Off")
            if XReflect == True:
                XReflect = False
            else:
                XReflect = True

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#YReflect":
            print("Auto Spin Toggled On/Off")
            if YReflect == True:
                YReflect = False
            else:
                YReflect = True

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#ZReflect":
            print("Auto Spin Toggled On/Off")
            if ZReflect == True:
                ZReflect = False
            else:
                ZReflect = True

        

        UI.process_events(event)

    UI.update(clock.tick(60)/1000)

    #Setting Ticks To 60 Per Second  
    clock.tick(120)

    scene.fill(LightBlue)

    #Drawing Axis 
    pygame.draw.line(scene,Grey,(Size[0]/2,0),(Size[0]/2,Size[1]))
    pygame.draw.line(scene,Grey,(0,Size[1]/2),(Size[0],Size[1]/2))

    '''
    Checks For Binary Variable Controls
    '''
    if euler==False:
        rotatedPoints=pointsRotate(Cube[0],axis,angle)
    else:
        rotatedPoints=eulerRotate(Cube[0],eulerAngle)
    '''
    Reflected Model
    '''
    #Reflects Model In True Axis
    if XReflect == True or YReflect == True or ZReflect == True:
        x=1
        y=1
        z=1
        if XReflect == True:
            x=-1
        if YReflect == True:
            y=-1
        if ZReflect == True:
            z=-1
        if x*y*z > 0:
            flipFaces = False
        if x*y*z < 0:
            flipFaces = True
        reflected = reflect(rotatedPoints, x, y, z)

        reflected = perspective(reflected, viewDistance, [x*pos[0],y*pos[1],z*pos[2]],zoffset)

        reflectedFaces = renderingList(reflected,Cube[1],flipFaces) 

        reflectedFaces = orderedPoints(reflected,reflectedFaces)

        render(reflected,reflectedFaces,scene,scale,offset)
    '''
    Regular Cube
    '''
    rotatedPoints=perspective(rotatedPoints, viewDistance,pos,zoffset)

    renderedFaces=renderingList(rotatedPoints,Cube[1],False)

    renderedFaces=orderedPoints(rotatedPoints,renderedFaces)

    render(rotatedPoints,renderedFaces,scene,scale,offset)

    '''
    Post Model Render GUI Checks, Text And Indicators
    '''
    #Draws Toggle Indicators
    if XReflect == True:
        pygame.draw.rect(scene,Green,((800,325),(145,25)))
    if YReflect == True:
        pygame.draw.rect(scene,Green,((800,350),(145,25)))
    if ZReflect == True:
        pygame.draw.rect(scene,Green,((800,375),(145,25)))

    if euler==False:
        pygame.draw.rect(scene,Green,((100, 625),(145,25)))
    else:
        pygame.draw.rect(scene,Green,((800, 625),(145,25)))
    if Spin == True:
        pygame.draw.rect(scene,Green,((450, 0),(100,50)))

    UI.draw_ui(scene)

    #Shows Prompts When GUI Is Hovered Over
    if event.type == pygame.MOUSEMOTION:
            if modelRect.collidepoint(event.pos):
                pygame.draw.rect(scene, Grey, modelRect_text)
                scene.blit(modelText,modelRect_text)
                
            if spinRect.collidepoint(event.pos):
                pygame.draw.rect(scene, Grey, spinRect_text)
                scene.blit(spinText,spinRect_text)

            if ReflectRect.collidepoint(event.pos):
                pygame.draw.rect(scene, Grey, ReflectRect_Text)
                scene.blit(ReflectText,ReflectRect_Text)

    PosText = pygame.font.SysFont("bahnschrift",20).render(f"Position",True,"Black") 
    pygame.draw.rect(scene, Grey, pygame.Rect((425, 625),(145,25)))
    scene.blit(PosText,pygame.Rect((465, 628),(145,25)))
    #Checks If Autospin Is On & Increments        
    if Spin == True:
        angle += increment
        eulerAngle[0] += increment
        eulerAngle[1] += increment
        eulerAngle[2] += increment

    pygame.display.update()


    
    

