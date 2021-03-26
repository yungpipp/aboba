"""
arcade_fun_skel.py

Общий код для написания программ,
  содержащих анимацию, при помощи
  библиотеки arcade

Как работать с этим файлом:

1. Скопируйте его в свою рабочую папку.

2. Переименуйте файл, чтобы его название
   отражало его предназначение.

3. Удалите этот комментарий
"""
# подключение библиотеки arcade
import arcade
import random
from normalDecorator import *

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

MOVEMENT_SPEED = 5

LEFT_VIEWPORT_MARGIN = 150
RIGHT_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

# Ширина окна
WINDOW_WIDTH = 1366
# Высота окна
WINDOW_HEIGHT = 768
# Заголовок окна
WINDOW_TITLE = " D!e "
# Цвет фона
WINDOW_COLOR = arcade.color.BLACK
# или можно так:
# WINDOW_COLOR = (255, 0, 0)




def draw_ufo(x,y):
    arcade.draw_ellipse_filled(x,y,140,70,(255,0,0))
    arcade.draw_circle_filled(x,y+40,45,(255,0,0))


def draw_cosmoairplane(x,y):
    arcade.draw_triangle_filled(x+150,y-40,x,y-180,x+300,y-180,(0,0,255))
    arcade.draw_triangle_filled(x+150,y-40,x+30,y-205,x+270,y-205,(0,0,255))






@decorator.setup
def setup(window):

   window.view_left=0
   window.view_bottom=0
   window.x=340
   window.y=700
   window.x1=random.randint(0,1366)
   window.y1=random.randint(0,768)

   window.x2=200
   window.y2=200

   window.x3=480
   window.y3=450

   window.x4=680
   window.y4=350

   window.x5=880
   window.y5=450


   window.vx=0
   window.vy=0
   window.vx1=-2
   window.vy1=-2





   window.count=0

   window.win=3




   """

   window.list=[]

   for i in range(100,600,100):
    window.list.append((i,200))

   for i in range(100,600,100):
    window.list.append((200,i))

   """




   window.time=0


   window.strike=[]


   window.pic=arcade.load_texture('unnamed.jpg')
   window.pic2=arcade.load_texture('уа.png')
   window.pic3=arcade.load_texture('fe.png')
   window.pic4=arcade.load_texture('ип.jpg')
   window.pic5=arcade.load_texture('d.png')
   window.pic6=arcade.load_texture('эй.png')
   window.pic7=arcade.load_texture('апчи.png')
   window.pic8=arcade.load_texture('start.png')
   window.pic9=arcade.load_texture('restart.png')
   window.pic10=arcade.load_texture('cursor.png')
   window.pic11=arcade.load_texture('next.png')
   window.pic1=arcade.load_texture('card.jpg')
   window.pic12=arcade.load_texture('ке.jpg')

   window.map=['хххххххххххххххх'
               'ххшшшххххххххххх',
               'ххшшшххххххххххх',
               'ххшшшшшшшшшшшшхх',
               'ххшшшшшшшшшшшшхх',
               'хххххшшшххшшшххх',
               'хххххшшшхшшшшххх',
               'хшшшшшшшшшшшшххх',
               'хшшшшшшшшшшшхххх',
               'хххххххххххххххх']





   window.mapList=[]
   window.mapList=arcade.SpriteList()
   for i in range(len(window.map)):
      for j in range(len(window.map[i])):
        if window.map[i][j]=='х':
          map=arcade.Sprite('ип.jpg',0.3)
          map.center_x=100*j
          map.center_y=800-100*i
          window.mapList.append(map)


   window.dyrnoi=arcade.Sprite('апчи.png',0.16)
   window.dyrnoi.center_x=320
   window.dyrnoi.center_y=140

   window.hero=arcade.Sprite('d.png',0.2)
   window.hero.center_x=320
   window.hero.center_y=600

   window.start=arcade.Sprite('start.png',0.2)
   window.start.center_x=680
   window.start.center_y=320

   window.restart=arcade.Sprite('restart.png',0.15)
   window.restart.center_x=400
   window.restart.center_y=150

   window.cursor=arcade.Sprite('cursor.png',0.1)
   window.cursor.center_x=700
   window.cursor.center_y=400

   window.next=arcade.Sprite('next.png',0.25)
   window.next.center_x=700
   window.next.center_y=150

   window.card=arcade.Sprite('card.jpg',0.1)
   window.card.center_x=800
   window.card.center_y=600


   window.dx=0
   window.dy=0

   window.coinList=[]
   window.coinList=arcade.SpriteList()

   window.rlist=[]
   window.rlist=arcade.SpriteList()
   window.rlist.append(window.restart)

   window.llist=[]
   window.llist=arcade.SpriteList()
   window.llist.append(window.start)

   window.nlist=[]
   window.nlist=arcade.SpriteList()
   window.nlist.append(window.next)

   window.clist=[]
   window.clist=arcade.SpriteList()
   window.clist.append(window.card)

   window.set_mouse_visible(False)



   for i in range(5):
     coin=arcade.Sprite('эй.png',0.02)
     coin_ps=False
     while not coin_ps:
       coin.center_x=random.randint(0,1366)
       coin.center_y=random.randint(0,768)
       wall_hit=arcade.check_for_collision_with_list(coin,window.mapList)
       coin_hit=arcade.check_for_collision_with_list(coin,window.coinList)
       if len(wall_hit)==0 and len(coin_hit)==0:
         coin_ps=True
     window.coinList.append(coin)

   window.aim=[]
   window.aim=arcade.SpriteList()
   window.aim.append(window.dyrnoi)












@decorator.update
def animate(window, time_delta):
    """
    Код этой функции вызывается каждый кадр.
    Переменная time_delta хранит сколько времени прошло
      с прошлого кадра.
    Разместите здесь код по анимации игровых объектов.
    НЕ РИСУЙТЕ В ЭТОЙ ФУНКЦИИ!

    Сотрите слово pass и вместо него напишите свой код.
    """

    """

    window.x+=2




    window.x+=window.vx
    if window.x>500:
      window.vx=-6

    if window.x<0:
      window.vx=+4

    """

    """

    if window.x==200 and window.y>=200 and window.y<300:
      window.y+=4

    elif window.y==300 and window.x>=200 and window.x<300:
      window.x+=4

    elif window.x==300 and window.y>=300 and window.y<400:
      window.y+=4

    elif window.y==400 and window.x>=300 and window.x<400:
      window.x+=4

    elif window.x==400 and window.y>=400 and window.y<500:
      window.y+=4

    elif window.y==500 and window.x>=400 and window.x<500:
      window.x+=4

    elif window.x==500 and window.y==500:
      window.x=200
      window.y=200

    """




    if window.win==0 or window.win==1 or window.win==2 or window.win==3:
      if window.x>1366 or window.x<0:
        window.hero.center_x-=window.dx

      if window.y>768 or window.y<0:
        window.hero.center_y-=window.dy




      window.hero.center_x+=window.dx
      window.hero.center_y+=window.dy


      window.dyrnoi.center_x+=window.vx
      window.dyrnoi.center_y+=window.vy


      if arcade.check_for_collision_with_list(window.dyrnoi,window.mapList):
        window.dyrnoi.center_x-=window.vx
        window.dyrnoi.center_y-=window.vy






      if arcade.check_for_collision_with_list(window.hero,window.mapList):
        window.hero.center_x-=window.dx
        window.hero.center_y-=window.dy



      hit=arcade.check_for_collision_with_list(window.hero,window.coinList)
      for coin in hit:
        coin.kill()
        window.count+=1






      if arcade.check_for_collision_with_list(window.hero,window.aim):
        window.win=1

      if window.count>=5:
        window.win=2


    if window.win==4:
      if window.x>1366 or window.x<0:
        window.hero.center_x-=window.dx

      if window.y>768 or window.y<0:
        window.hero.center_y-=window.dy




      window.hero.center_x+=window.dx
      window.hero.center_y+=window.dy


      window.dyrnoi.center_x+=window.vx
      window.dyrnoi.center_y+=window.vy


      if arcade.check_for_collision_with_list(window.dyrnoi,window.mapList):
        window.dyrnoi.center_x-=window.vx
        window.dyrnoi.center_y-=window.vy






      if arcade.check_for_collision_with_list(window.hero,window.mapList):
        window.hero.center_x-=window.dx
        window.hero.center_y-=window.dy



      hit=arcade.check_for_collision_with_list(window.hero,window.coinList)
      for coin in hit:
        coin.kill()
        window.count+=1






      if arcade.check_for_collision_with_list(window.hero,window.aim):
        window.win=6

      if window.count>=5:
        window.win=5

    if window.win==7:
      if window.x>1366 or window.x<0:
        window.hero.center_x-=window.dx

      if window.y>768 or window.y<0:
        window.hero.center_y-=window.dy




      window.hero.center_x+=window.dx
      window.hero.center_y+=window.dy



      if arcade.check_for_collision_with_list(window.hero,window.mapList):
        window.hero.center_x-=window.dx
        window.hero.center_y-=window.dy


      if arcade.check_for_collision_with_list(window.hero,window.clist):
        window.win=8


    if window.win==9:



      if arcade.check_for_collision_with_list(window.hero,window.mapList):
        window.hero.center_x-=window.dx
        window.hero.center_y-=window.dy

      if window.hero.center_y==350 and window.hero.center_x>=100 and window.hero.center_x<450:
        window.hero.center_x+=1

      if window.hero.center_y==350 and window.hero.center_x>=400 and window.hero.center_x<450:
        window.dyrnoi.center_x-=2

      if window.dyrnoi.center_y==350 and window.dyrnoi.center_x<=1360 and window.dyrnoi.center_x>450:
        window.dyrnoi.center_x-=10

      if arcade.check_for_collision_with_list(window.hero,window.aim):
        window.win=10

    changed = False

    # Scroll left
    left_boundary = window.view_left + LEFT_VIEWPORT_MARGIN
    if window.hero.left < left_boundary:
      window.view_left -= left_boundary - window.hero.left
      changed = True

    # Scroll right
    right_boundary = window.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
    if window.hero.right > right_boundary:
      window.view_left += window.hero.right - right_boundary
      changed = True

    # Scroll up
    top_boundary = window.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
    if window.hero.top > top_boundary:
      window.view_bottom += window.hero.top - top_boundary
      changed = True

    # Scroll down

    bottom_boundary = window.view_bottom + BOTTOM_VIEWPORT_MARGIN
    if window.hero.bottom < bottom_boundary:
      window.view_bottom -= bottom_boundary - window.hero.bottom
      changed = True

    if changed:
      # Only scroll to integers. Otherwise we end up with pixels that
      # don't line up on the screen
      window.view_bottom = int(window.view_bottom)
      window.view_left = int(window.view_left)

      # Do the scrolling
      arcade.set_viewport(window.view_left, SCREEN_WIDTH + window.view_left, window.view_bottom, SCREEN_HEIGHT + window.view_bottom)











@decorator.key_press
def on_key_press(window, key, key_modifiers):
    """
    Код этой функции позволяет обрабатывать нажатия на клавиши.
    Переменная key хранит нажатую клавишу.
    Переменная key_modifiers хранит нажатые клавиши-модификаторы,
      такие как Shift или Alt.
    Клавиши и модификаторы могут быть использованы из модуля arcade.key
      (https://github.com/pvcraven/arcade/blob/master/arcade/key/__init__.py)
    Разместите здесь код по управлению игровых объектов с клавиатуры.
    НЕ РИСУЙТЕ В ЭТОЙ ФУНКЦИИ!

    Сотрите слово pass и вместо него напишите свой код.
    """
    if key==arcade.key.D:
      window.dx=5

    if key==arcade.key.A:
      window.dx=-5

    if key==arcade.key.W:
      window.dy=5

    if key==arcade.key.S:
      window.dy=-5

    if key==arcade.key.SPACE:
      window.strike.append((window.x+300,window.y+50))

    if key==arcade.key.RIGHT:
      window.vx=2

    if key==arcade.key.LEFT:
      window.vx=-2

    if key==arcade.key.UP:
      window.vy=2

    if key==arcade.key.DOWN:
      window.vy=-2



@decorator.key_release
def on_key_release(window, key, key_modifiers):
    if key==arcade.key.D:
      window.dx=0

    if key==arcade.key.A:
      window.dx=0

    if key==arcade.key.W:
      window.dy=0

    if key==arcade.key.S:
      window.dy=0

    if key==arcade.key.RIGHT:
      window.vx=0

    if key==arcade.key.LEFT:
      window.vx=0

    if key==arcade.key.UP:
      window.vy=0

    if key==arcade.key.DOWN:
      window.vy=0


@decorator.draw
def draw(window):
    """
    Код этой функции вызывается каждый кадр.
    Разместите здесь код по рисованию игровых объектов.
    НЕ ПРОПИСЫВАЙТЕ КОД АНИМАЦИИ В ЭТОЙ ФУНКЦИИ!

    Сотрите слово pass и вместо него напишите свой код.
    """


    """

    arcade.draw_circle_filled(window.x+260,window.y+100,200,(250,255,0))
    arcade.draw_circle_filled(window.x+860,window.y+100,200,(250,255,0))

    """





    """

    draw_cosmoairplane(window.x+300,window.y+50)


    draw_ufo(window.x1+200,window.y1+200)
    draw_ufo(window.x2+200,window.y2+200)
    draw_ufo(window.x3+200,window.y3+200)
    draw_ufo(window.x4+200,window.y4+200)
    draw_ufo(window.x5+200,window.y5+200)
    arcade.draw_line(200,1,200,768,(250,0,0),10)
    arcade.draw_line(1166,1,1166,768,(250,0,0),10)

    """

    """
    if window.win == 0:
      arcade.draw_rectangle_filled(window.x1,window.y1,30,30,(255,255,255))
      arcade.draw_circle_filled(window.x,window.y,60,(255,250,0))
      arcade.draw_text(str(window.count),1200,600,(250,250,250),20)

    elif window.win == 1:
      arcade.draw_text("PADORU PADORU!!!",420,380,(255,0,0),50)
      arcade.draw_text("(hashire sori yo, kaze no you ni)",560,300,(255,255,255),15)
      arcade.draw_text("tsukimihara wo",640,100,(0,255,0),10)

    """

    """

    for i in range(100,800,100):
      arcade.draw_circle_filled(200,i,60,(255,255,0))
      arcade.draw_circle_filled(i,200,60,(255,255,0))
      arcade.draw_circle_filled(600,i,60,(255,255,0))
      arcade.draw_circle_filled(i,600,60,(255,255,0))

    """

    """

    for i in range(len(window.list)):
      x,y=window.list[i]
      arcade.draw_rectangle_filled(x,y,50,50,(255,0,0))

    """

    """

    if window.win == 0:

      arcade.draw_point(124,723,(255,255,250),5)
      arcade.draw_point(234,345,(255,255,250),5)
      arcade.draw_point(832,617,(255,255,250),5)
      arcade.draw_point(85,276,(255,255,250),5)
      arcade.draw_point(945,24,(255,255,250),5)
      arcade.draw_point(845,143,(255,255,250),5)
      arcade.draw_point(765,345,(255,255,250),5)
      arcade.draw_point(345,742,(255,255,250),5)
      arcade.draw_point(311,483,(255,255,250),5)
      arcade.draw_point(741,23,(255,255,250),5)
      arcade.draw_point(1065,36,(255,255,250),5)
      arcade.draw_point(356,257,(255,255,250),5)
      arcade.draw_point(554,45,(255,255,250),5)
      arcade.draw_point(567,547,(255,255,250),5)
      arcade.draw_point(56,672,(255,255,250),5)
      arcade.draw_point(675,68,(255,255,250),5)
      arcade.draw_point(856,588,(255,255,250),5)
      arcade.draw_point(1027,67,(255,255,250),5)
      arcade.draw_point(563,257,(255,255,250),5)
      arcade.draw_point(1242,459,(255,255,250),5)
      arcade.draw_point(571,79,(255,255,250),5)
      arcade.draw_point(485,386,(255,255,250),5)








      for i in range(len(window.aim)):
        x,y,z=window.aim[i]
        arcade.draw_texture_rectangle(x,y,250,250,window.pic3)

      arcade.draw_texture_rectangle(window.x+150,window.y-50,200,200,window.pic2)

      for i in range(len(window.strike)):
        x,y=window.strike[i]
        arcade.draw_texture_rectangle(x-150,y,30,30,window.pic1)

      arcade.draw_text(str(window.count),1200,600,(250,250,250),20)


    elif window.win == 1:
      arcade.draw_text("PADORU PADORU!!!",420,380,(255,0,0),50)
      arcade.draw_text("(hashire sori yo, kaze no you ni)",560,300,(255,255,255),15)
      arcade.draw_text("tsukimihara wo",640,100,(0,255,0),10)
      arcade.draw_texture_rectangle(683,550,200,200,window.pic)

    """


    """

    for i in range(len(window.map)):
      for j in range(len(window.map[i])):
        if window.map[i][j]=='х':
          map=arcade.Sprite('window.pic4',0.3)
          map.center_x=100*j
          map.center_y=800-100*i
          window.mapList.append(map)

    """

    if window.win == 3:
      arcade.draw_text('ДУРКА.exe',540,600,(255,0,0),50)
      arcade.draw_circle_filled(680,320,100,(255,255,255))
      window.start.draw()
      window.cursor.draw()



    elif window.win == 0:
      window.hero.draw()
      window.mapList.draw()
      window.coinList.draw()
      window.dyrnoi.draw()
      arcade.draw_text('дурка "Glaza"',240,730,(255,0,0),20)
      arcade.draw_text('КПП №1',700,300,(255,0,0),30)
      arcade.draw_text(str(window.count),1200,600,(250,250,250),20)


    elif window.win == 1:
      arcade.draw_text('Вас съел дурной...',440,380,(255,0,0),50)
      arcade.draw_text('вы o6re4enbI',610,300,(255,0,0),20)
      arcade.draw_circle_filled(400,150,50,(255,255,255))
      window.restart.draw()
      window.cursor.draw()


    elif window.win == 2:
      arcade.draw_text('Здесь все, пошли дальше',360,380,(255,250,250),50)
      arcade.draw_circle_filled(400,150,50,(255,255,255))
      window.restart.draw()
      arcade.draw_circle_filled(700,150,70,(255,255,255))
      window.next.draw()
      window.cursor.draw()

    elif window.win == 4:
      window.mapList.draw()
      window.coinList.draw()
      window.dyrnoi.draw()
      window.hero.draw()
      arcade.draw_text('КПП №2',100,700,(255,0,0),20)


    elif window.win == 5:
      arcade.draw_text('Здесь все, пошли дальше',360,380,(255,250,250),50)
      arcade.draw_circle_filled(400,150,50,(255,255,255))
      window.restart.draw()
      arcade.draw_circle_filled(700,150,70,(255,255,255))
      window.next.draw()
      window.cursor.draw()

    elif window.win == 6:
      arcade.draw_text('Вас съел дурной...',440,380,(255,0,0),50)
      arcade.draw_text('вы o6re4enbI',610,300,(255,0,0),20)
      arcade.draw_circle_filled(400,150,50,(255,255,255))
      window.restart.draw()
      window.cursor.draw()

    elif window.win==7:
      window.mapList.draw()
      window.hero.draw()
      window.card.draw()

    elif window.win==8:
      arcade.draw_text('Ключ карта найдена. Пора сваливать.',400,380,(255,250,250),30)
      arcade.draw_circle_filled(700,150,70,(255,255,255))
      window.next.draw()
      window.cursor.draw()

    elif window.win==9:
      window.mapList.draw()
      window.hero.draw()
      window.dyrnoi.draw()

    elif window.win==10:
      arcade.draw_text('о͏͏̡͠6̨̧͜͟р̢̧̢̛̕е̶̛̕͝4҉e̷̶͘͢͠n̡̨͡',375,380,(255,0,0),50)





def setup1(window):
    window.x=340
    window.y=700
    window.x1=random.randint(0,1366)
    window.y1=random.randint(0,768)

    window.x2=200
    window.y2=200

    window.x3=480
    window.y3=450

    window.x4=680
    window.y4=350

    window.x5=880
    window.y5=450


    window.vx=0
    window.vy=0
    window.vx1=-2
    window.vy1=-2





    window.count=0

    window.win=4



    window.time=0


    window.strike=[]


    window.pic=arcade.load_texture('unnamed.jpg')
    window.pic2=arcade.load_texture('уа.png')
    window.pic3=arcade.load_texture('fe.png')
    window.pic4=arcade.load_texture('ип.jpg')
    window.pic5=arcade.load_texture('d.png')
    window.pic6=arcade.load_texture('эй.png')
    window.pic7=arcade.load_texture('апчи.png')
    window.pic8=arcade.load_texture('start.png')
    window.pic9=arcade.load_texture('restart.png')
    window.pic10=arcade.load_texture('cursor.png')
    window.pic11=arcade.load_texture('next.png')
    window.pic1=arcade.load_texture('card.jpg')
    window.pic12=arcade.load_texture('ке.jpg')

    window.map=['ххххххххххххххххх',
                'ххххххххххххххххх',
                'хшшшшшшшшшххххххх',
                'хшшшшшшшшшххххххх',
                'хшшшхххшшшххххххх',
                'хшшшхххшшшххххххх',
                'хшшшшшшшшшшшшшшшх',
                'хшшшшшшшшшшшшшшшх',
                'ххххххххххххххххх']





    window.mapList=[]
    window.mapList=arcade.SpriteList()
    for i in range(len(window.map)):
       for j in range(len(window.map[i])):
         if window.map[i][j]=='х':
           map=arcade.Sprite('ип.jpg',0.3)
           map.center_x=100*j
           map.center_y=800-100*i
           window.mapList.append(map)


    window.dyrnoi=arcade.Sprite('апчи.png',0.16)
    window.dyrnoi.center_x=320
    window.dyrnoi.center_y=140

    window.hero=arcade.Sprite('d.png',0.2)
    window.hero.center_x=200
    window.hero.center_y=550

    window.start=arcade.Sprite('start.png',0.2)
    window.start.center_x=680
    window.start.center_y=320

    window.restart=arcade.Sprite('restart.png',0.15)
    window.restart.center_x=400
    window.restart.center_y=150

    window.cursor=arcade.Sprite('cursor.png',0.1)
    window.cursor.center_x=700
    window.cursor.center_y=400

    window.next=arcade.Sprite('next.png',0.25)
    window.next.center_x=700
    window.next.center_y=150

    window.card=arcade.Sprite('card.jpg',0.1)
    window.card.center_x=700
    window.card.center_y=1000

    window.dx=0
    window.dy=0

    window.coinList=[]
    window.coinList=arcade.SpriteList()

    window.rlist=[]
    window.rlist=arcade.SpriteList()
    window.rlist.append(window.restart)

    window.llist=[]
    window.llist=arcade.SpriteList()
    window.llist.append(window.start)

    window.nlist=[]
    window.nlist=arcade.SpriteList()
    window.nlist.append(window.next)

    window.clist=[]
    window.clist=arcade.SpriteList()
    window.clist.append(window.card)




    window.set_mouse_visible(False)



    for i in range(5):
      coin=arcade.Sprite('эй.png',0.02)
      coin_ps=False
      while not coin_ps:
        coin.center_x=random.randint(0,1366)
        coin.center_y=random.randint(0,768)
        wall_hit=arcade.check_for_collision_with_list(coin,window.mapList)
        coin_hit=arcade.check_for_collision_with_list(coin,window.coinList)
        if len(wall_hit)==0 and len(coin_hit)==0:
          coin_ps=True
      window.coinList.append(coin)

    window.aim=[]
    window.aim=arcade.SpriteList()
    window.aim.append(window.dyrnoi)


def setup2(window):
    window.x=340
    window.y=700
    window.x1=random.randint(0,1366)
    window.y1=random.randint(0,768)

    window.x2=200
    window.y2=200

    window.x3=480
    window.y3=450

    window.x4=680
    window.y4=350

    window.x5=880
    window.y5=450


    window.vx=0
    window.vy=0
    window.vx1=-2
    window.vy1=-2





    window.count=0

    window.win=7



    window.time=0


    window.strike=[]


    window.pic=arcade.load_texture('unnamed.jpg')
    window.pic2=arcade.load_texture('уа.png')
    window.pic3=arcade.load_texture('fe.png')
    window.pic4=arcade.load_texture('ип.jpg')
    window.pic5=arcade.load_texture('d.png')
    window.pic6=arcade.load_texture('эй.png')
    window.pic7=arcade.load_texture('апчи.png')
    window.pic8=arcade.load_texture('start.png')
    window.pic9=arcade.load_texture('restart.png')
    window.pic10=arcade.load_texture('cursor.png')
    window.pic11=arcade.load_texture('next.png')
    window.pic1=arcade.load_texture('card.jpg')
    window.pic12=arcade.load_texture('ке.jpg')

    window.map=['хххххххххххххххх',
                'ххххххххххшшшшхх',
                'хххххххшшшшшшшхх',
                'хххххххшшшшшшшхх',
                'хххххххшшшхххххх',
                'хххххххшшшхххххх',
                'хшшшшшшшшшшшшшшшх',
                'хшшшшшшшшшшшшшшшх',
                'хххххххгггхххххх',
                'хшшшшшшшшшшшшшшх',
                'хшшшшшшшшшшшшшшх',
                'хххххххххххххххх']





    window.mapList=[]
    window.mapList=arcade.SpriteList()
    for i in range(len(window.map)):
       for j in range(len(window.map[i])):
         if window.map[i][j]=='х':
           map=arcade.Sprite('ип.jpg',0.3)
           map.center_x=100*j
           map.center_y=800-100*i
           window.mapList.append(map)

    for i in range(len(window.map)):
       for j in range(len(window.map[i])):
         if window.map[i][j]=='г':
           map=arcade.Sprite('ке.jpg',0.3)
           map.center_x=100*j
           map.center_y=800-100*i
           window.mapList.append(map)


    window.dyrnoi=arcade.Sprite('апчи.png',0.16)
    window.dyrnoi.center_x=320
    window.dyrnoi.center_y=140

    window.hero=arcade.Sprite('d.png',0.2)
    window.hero.center_x=200
    window.hero.center_y=150

    window.start=arcade.Sprite('start.png',0.2)
    window.start.center_x=680
    window.start.center_y=320

    window.restart=arcade.Sprite('restart.png',0.15)
    window.restart.center_x=400
    window.restart.center_y=150

    window.cursor=arcade.Sprite('cursor.png',0.1)
    window.cursor.center_x=700
    window.cursor.center_y=400

    window.next=arcade.Sprite('next.png',0.25)
    window.next.center_x=700
    window.next.center_y=150

    window.card=arcade.Sprite('card.jpg',0.1)
    window.card.center_x=1100
    window.card.center_y=700

    window.dx=0
    window.dy=0

    window.coinList=[]
    window.coinList=arcade.SpriteList()

    window.rlist=[]
    window.rlist=arcade.SpriteList()
    window.rlist.append(window.restart)

    window.llist=[]
    window.llist=arcade.SpriteList()
    window.llist.append(window.start)

    window.nlist=[]
    window.nlist=arcade.SpriteList()
    window.nlist.append(window.next)

    window.clist=[]
    window.clist=arcade.SpriteList()
    window.clist.append(window.card)



    window.set_mouse_visible(False)



    for i in range(5):
      coin=arcade.Sprite('эй.png',0.02)
      coin_ps=False
      while not coin_ps:
        coin.center_x=random.randint(0,1366)
        coin.center_y=random.randint(0,768)
        wall_hit=arcade.check_for_collision_with_list(coin,window.mapList)
        coin_hit=arcade.check_for_collision_with_list(coin,window.coinList)
        if len(wall_hit)==0 and len(coin_hit)==0:
          coin_ps=True
      window.coinList.append(coin)

    window.aim=[]
    window.aim=arcade.SpriteList()
    window.aim.append(window.dyrnoi)





def setup3(window):
    window.x=340
    window.y=700
    window.x1=random.randint(0,1366)
    window.y1=random.randint(0,768)

    window.x2=200
    window.y2=200

    window.x3=480
    window.y3=450

    window.x4=680
    window.y4=350

    window.x5=880
    window.y5=450


    window.vx=0
    window.vy=0
    window.vx1=-2
    window.vy1=-2





    window.count=0

    window.win=9



    window.time=0


    window.strike=[]


    window.pic=arcade.load_texture('unnamed.jpg')
    window.pic2=arcade.load_texture('уа.png')
    window.pic3=arcade.load_texture('fe.png')
    window.pic4=arcade.load_texture('ип.jpg')
    window.pic5=arcade.load_texture('d.png')
    window.pic6=arcade.load_texture('эй.png')
    window.pic7=arcade.load_texture('апчи.png')
    window.pic8=arcade.load_texture('start.png')
    window.pic9=arcade.load_texture('restart.png')
    window.pic10=arcade.load_texture('cursor.png')
    window.pic11=arcade.load_texture('next.png')
    window.pic1=arcade.load_texture('card.jpg')
    window.pic12=arcade.load_texture('ке.jpg')

    window.map=['хххххххххххххххх',
                'хххххххххххххххх',
                'хххххххххххххххх',
                'хххххххххххххххх',
                'шшшшшшшшшшшшшшшш',
                'шшшшшшшшшшшшшшшш',
                'хххххххххххххххх',
                'хххххххххххххххх',
                'хххххххххххххххх',
                'хххххххххххххххх']





    window.mapList=[]
    window.mapList=arcade.SpriteList()
    for i in range(len(window.map)):
       for j in range(len(window.map[i])):
         if window.map[i][j]=='х':
           map=arcade.Sprite('ип.jpg',0.3)
           map.center_x=100*j
           map.center_y=800-100*i
           window.mapList.append(map)


    window.dyrnoi=arcade.Sprite('апчи.png',0.16)
    window.dyrnoi.center_x=1400
    window.dyrnoi.center_y=350

    window.hero=arcade.Sprite('d.png',0.2)
    window.hero.center_x=100
    window.hero.center_y=350

    window.start=arcade.Sprite('start.png',0.2)
    window.start.center_x=680
    window.start.center_y=320

    window.restart=arcade.Sprite('restart.png',0.15)
    window.restart.center_x=400
    window.restart.center_y=150

    window.cursor=arcade.Sprite('cursor.png',0.1)
    window.cursor.center_x=700
    window.cursor.center_y=400

    window.next=arcade.Sprite('next.png',0.25)
    window.next.center_x=700
    window.next.center_y=150

    window.card=arcade.Sprite('card.jpg',0.1)
    window.card.center_x=1100
    window.card.center_y=700

    window.dx=0
    window.dy=0

    window.coinList=[]
    window.coinList=arcade.SpriteList()

    window.rlist=[]
    window.rlist=arcade.SpriteList()
    window.rlist.append(window.restart)

    window.llist=[]
    window.llist=arcade.SpriteList()
    window.llist.append(window.start)

    window.nlist=[]
    window.nlist=arcade.SpriteList()
    window.nlist.append(window.next)

    window.clist=[]
    window.clist=arcade.SpriteList()
    window.clist.append(window.card)



    window.set_mouse_visible(False)



    for i in range(5):
      coin=arcade.Sprite('эй.png',0.02)
      coin_ps=False
      while not coin_ps:
        coin.center_x=random.randint(0,1366)
        coin.center_y=random.randint(0,768)
        wall_hit=arcade.check_for_collision_with_list(coin,window.mapList)
        coin_hit=arcade.check_for_collision_with_list(coin,window.coinList)
        if len(wall_hit)==0 and len(coin_hit)==0:
          coin_ps=True
      window.coinList.append(coin)

    window.aim=[]
    window.aim=arcade.SpriteList()
    window.aim.append(window.dyrnoi)
























@decorator.mouse_moution
def mouse_moution(window, x, y, dx, dy):
    window.cursor.center_x=x
    window.cursor.center_y=y

@decorator.mouse_release
def mouse_release(window, x, y, button, modifiers):
    pass

@decorator.mouse_press
def mouse_press(window, x, y, button, modifiers):
    if window.win==3:
      if arcade.check_for_collision_with_list(window.cursor,window.llist):
        window.win=0

    if window.win==1 or window.win==2:
      if arcade.check_for_collision_with_list(window.cursor,window.rlist,):
        setup(window)
        window.win=0

    if window.win==2:
      if arcade.check_for_collision_with_list(window.cursor,window.nlist):
        setup1(window)

    if window.win==5 or window.win==6:
      if arcade.check_for_collision_with_list(window.cursor,window.rlist,):
        setup1(window)
        window.win=4


    if window.win==5:
      if arcade.check_for_collision_with_list(window.cursor,window.nlist):
        setup2(window)

    if window.win==8:
      if arcade.check_for_collision_with_list(window.cursor,window.nlist):
        setup3(window)





# запуск программы
decorator.run(WINDOW_WIDTH, WINDOW_HEIGHT, title=WINDOW_TITLE, background_color=WINDOW_COLOR)
