# подключение библиотеки arcade
import arcade

# Ширина окна
WINDOW_WIDTH = 1366
# Высота окна
WINDOW_HEIGHT = 768
# Заголовок окна
WINDOW_TITLE = "it's over 9000"
# Цвет фона
WINDOW_COLOR = arcade.color.BLACK
# или можно так:
# WINDOW_COLOR = (255, 0, 0)

# Создание окна программы
arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
# Задание цвета фона окна
arcade.set_background_color(WINDOW_COLOR)

arcade.start_render()

# Код рисования пишите здесь
# vvvvvvvvvvvvvvvvv

"""
arcade.draw_circle_filled(190,590,30,(0,0,255))
arcade.draw_circle_filled(490,600,30,(0,0,255))
arcade.draw_circle_filled(500,215,30,(0,0,255))
arcade.draw_circle_filled(200,200,30,(0,0,255))
arcade.draw_polygon_filled(((200,200),(500,215),(490,600),(190,590)),(255,0,0))
arcade.draw_ellipse_filled(400,300,200,150,(0,255,0))
arcade.draw_ellipse_filled(300,400,50,50,(150,0,255))
arcade.draw_ellipse_filled(250,590,100,200,(255,100,0),30)
arcade.draw_text("ага, вы попали в ловушку Джокера.",1100,50,(255,250,250))
arcade.draw_text("а",10,750,(255,250,250))
arcade.draw_text("это что",550,450,(255,250,250))
arcade.draw_text("morkov(каррот)",300,620,(255,250,250))
arcade.draw_text("арбуз без полосок",350,350,(255,250,250))
"""

"""

arcade.draw_line(200,1,200,768,(250,0,0),10)
arcade.draw_line(1166,1,1166,768,(250,0,0),10)
arcade.draw_triangle_filled(650,160,500,20,800,20,(0,250,0))
arcade.draw_line(700,100,700,150,(0,255,0),10)
arcade.draw_line(600,100,600,150,(0,255,0),10)
arcade.draw_line(550,50,550,100,(0,255,0),10)
arcade.draw_line(750,50,750,100,(0,255,0),10)
arcade.draw_line(650,160,650,200,(255,0,0),10)
arcade.draw_ellipse_filled()

"""

"""

x=200
y=300


arcade.draw_ellipse_filled(x,y,250,500,(255,0,0),90)
    arcade.draw_circle_filled(x+15,y+100,140,(255,0,0))

    """

    """

    x=300
    y=400
    def draw_ufo(x,y):
        arcade.draw_ellipse_filled(x,y,200,200,(255,0,0))
        arcade.draw_circle_filled(x+15,y+100,50,(255,0,0))
    draw_ufo(200, 500)
    draw_ufo(500, 500)

    """

    """

    x=500
    y=200

def draw_cosmoairplane(x,y):
    arcade.draw_triangle_filled(x+150,y-40,x,y-180,x+300,y-180,(0,250,0))
    arcade.draw_line(700,100,700,150,(0,255,0),10)
    arcade.draw_line(600,100,600,150,(0,255,0),10)
    arcade.draw_line(550,50,550,100,(0,255,0),10)
    arcade.draw_line(750,50,750,100,(0,255,0),10)
    arcade.draw_line(650,160,650,200,(255,0,0),10)
draw_cosmoairplane(500,200)
draw_cosmoairplane(1000,200)
draw_cosmoairplane(100,200)

""" 


# ^^^^^^^^^^^^^^
# Код рисования пишите здесь

arcade.finish_render()

# Запуск программы
arcade.run()
