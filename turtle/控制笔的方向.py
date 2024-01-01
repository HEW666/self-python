import turtle

turtle.title('控制笔的方向')

turtle.pencolor('red')
turtle.left(45)  # 向左旋转指定角度
turtle.forward(50)  # 移动距离

turtle.pencolor('green')
turtle.right(90)  # 向右旋转指定角度
turtle.forward(200)

turtle.pencolor('purple')
turtle.setheading(10)  # 设置绝对角度值指定度数
turtle.forward(100)

turtle.mainloop()
