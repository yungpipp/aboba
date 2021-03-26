field= [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]
winX = False
winO = False
draw = False
player = "X"
def print_field():
    for i in range(3):
        print(field[i][0]+"|"+field[i][1]+"|"+field[i][2])
print_field()
l=0
def turn():
        print("Ходит ",player)
        p=int(input('p='))
        p1=int(input('p1='))
        while field[p][p1]!=' ':
                p=int(input('p='))
                p1=int(input('p1='))
        field[p][p1]=player
        print_field()
while not winX or not winO:
        if draw:
                print('ничья')
                break
        if winX:
                print('X win')
                break
        if winO:
                print('O win')
                break
        draw=True
        turn()
        if field[0][0]=='X' and field[1][1]=='X' and field[2][2]=='X':
                winX=True
        if field[0][2]=='X' and field[1][1]=='X' and field[2][0]=='X':
                winX=True
        if field[0][0]=='X' and field[0][1]=='X' and field[0][2]=='X':
                winX=True
        if field[2][0]=='X' and field[2][1]=='X' and field[2][2]=='X':
                winX=True
        if field[0][0]=='X' and field[1][0]=='X' and field[2][0]=='X':
                winX=True
        if field[0][2]=='X' and field[1][2]=='X' and field[2][2]=='X':
                winX=True
        if field[0][0]=='O' and field[1][1]=='O' and field[2][2]=='O':
                winO=True
        if field[0][2]=='O' and field[1][1]=='O' and field[2][0]=='O':
                winO=True
        if field[0][0]=='O' and field[0][1]=='O' and field[0][2]=='O':
                winO=True
        if field[2][0]=='O' and field[2][1]=='O' and field[2][2]=='O':
                winO=True
        if field[0][0]=='O' and field[1][0]=='O' and field[2][0]=='O':
                winO=True
        if field[0][2]=='O' and field[1][2]=='O' and field[2][2]=='O':
                winO=True
        if player=='X':
                player='O'
        else:
                player='X'
        for i in range(0,len(field)):
                for j in range(0,len(field[i])):
                        if field[i][j]==" ":
                                draw=False