import turtle

turtle.title('控制笔的移动')  # 标题
turtle.setup(800, 600)  # 设置画布的宽度和高度
turtle.pencolor('red')  # 设置画笔画出的线的颜色
turtle.width(5)  # 设置线宽
turtle.speed(2)  # 设置笔移动的速度(速度值是1-10逐渐变快；0 对应的速度最

turtle.back(230)  # 控制笔后退指定距离

turtle.sety(20)  # 控制笔移动到指定位置 (y坐标)

turtle.setx(220)  # 控制笔移动到指定位置 (x坐标)

turtle.goto(-100, -200)  # 控制笔移动到指定位置(x坐标, y坐标)

turtle.home()  # 笔回到初始状态（回到初始位置和初始方向）

turtle.mainloop()  # 让画布一直存在，这句代码需要放在最后
