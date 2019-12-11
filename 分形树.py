import turtle as t
import random
def draw_tree(size):
    t.pensize(5)
    t.speed(1000)
    if size > 10:
            # 右边
        t.forward(size)
        t.right(30)
        draw_tree(size-random.randint(20,30))
        # 左边
        t.left(60)
        draw_tree(size-random.randint(20,30))
        # 回到之前的树枝
        t.right(30)
        # 给最后的树枝画绿色
        t.color("brown")
        if size<= 50:
            t.color('yellow')
        t.backward(size)
     # 传递这时候的坐标


#画树干
t.penup()
t.left(90)
t.backward(400)
t.pensize(30)
t.color("Chocolate")
t.pendown()
t.begin_fill()
t.forward(100)
t.pensize(20)   #树干变细
t.forward(100)
t.speed(5000)
draw_tree(150)
t.exitonclick()

