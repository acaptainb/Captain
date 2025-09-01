import turtle as t

t.setup(1500, 400)

def diamond_sign():
    '''
    :return:
    '''
    t.pencolor('black')
    t.pensize(3)
    t.fillcolor("yellow")
    t.begin_fill()
    t.left(45)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(135)
    t.end_fill()
    t.up()
# diamond_sign()
def sign():
    '''
    :return:
    '''
    diamond_sign()
    t.pensize(18)
    t.forward(140)
    t.left(90)
    t.forward(70)
    t.left(180)
    t.down()
    t.forward(160)
    t.right(180)
    t.forward(85)
def sign1():
    '''
     :return:
    '''
    sign()
    t.right(90)
    t.forward(60)
    t.up()
    # t.left(180)
    # t.forward(195)


def own_sign():

    t.forward(50)
    t.down()
    sign()
    t.up()
    t.left(90)
    t.forward(80)
    t.left(180)
    t.down()
    t.forward(160)
    t.up()

def sign2():
    '''
    :return:
    '''
    t.down()
    sign()
    t.right(90)
    t.forward(60)
    t.back(60)

    t.left(180)
    t.up()

def sign3():
    '''
    :return:
    '''
    t.down()
    sign()
    t.forward(75)
    t.left(90)

    t.back(50)
    t.forward(100)
    # t.left(90)
    t.up()


def main():
    t.speed(0)
    sign1()
    t.left(180)
    t.forward(195)
    own_sign()
    t.forward(90)
    sign2()
    t.forward(820)
    sign3()


main()
t.done()