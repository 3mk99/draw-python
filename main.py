import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def draw_circle():
    turtle.circle(50)

def draw_shape(shape_name):
    if shape_name.lower() == 'square':
        draw_square()
    elif shape_name.lower() == 'triangle':
        draw_triangle()
    elif shape_name.lower() == 'circle':
        draw_circle()
    else:
        print("Invalid shape name!")

# الدالة الرئيسية
def main():
    turtle.speed(1)

    print("What shape do you want to draw?")
    shape = input("Please enter the shape name in English (square, triangle, circle): ")

    draw_shape(shape)

    turtle.done()

if __name__ == "__main__":
    main()
