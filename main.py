# # This code here shows how you can extract the colors of an image. really interesting

# import colorgram

# colors = colorgram.extract("image.jpg.jpg", 50)
# # print(colors)

# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

#e for extracted
e_colors = [(197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68), (228, 160, 47), (243, 247, 253),
            (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11), (242, 34, 164), (226, 19, 120), (74, 9, 31),
            (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10), (18, 18, 43), (52, 211, 230), (11, 228, 239),
            (80, 73, 214), (238, 156, 217), (73, 212, 168), (81, 234, 202), (61, 233, 241), (5, 67, 42), (219, 89, 48),
            (174, 179, 233), (235, 169, 163), (8, 245, 219), (249, 8, 54), (7, 82, 114), (23, 56, 233), (244, 14, 14)]

import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255)
rashid = turtle_module.Turtle()
rashid.speed(0)
rashid.hideturtle()
rashid.penup()
rashid.setheading(225)
rashid.forward(300)
rashid.setheading(0)

dots = 100

for dot_count in range(1, dots + 1):
    rashid.dot(15, random.choice(e_colors))
    rashid.forward(50)
    if dot_count % 10 == 0:
        rashid.setheading(90)
        rashid.forward(50)
        rashid.setheading(180)
        rashid.forward(500)
        rashid.setheading(0)

Screen().exitonclick()
