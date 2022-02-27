from rectangle import Rectangle, Square, Circle



recrt_1 = Rectangle(3,4)
recrt_2 = Rectangle(12,5)

print("прямоугольник  1 =",recrt_1.get_area())
print("прямоугольник 2 = ",recrt_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print("квадрат 1 = ",square_1.get_area_square(),"квадрат 2 =",square_2.get_area_square())

Ci = Circle(4)
print("круг =",Ci.get_area_circle())

figures = [recrt_1, recrt_2, square_1, square_2]
for figure in figures:
    if isinstance(figure,Square): #функция isinstance, поддерживающая
        # наследование. Она проверяет, является ли аргумент
        # объекта экземпляром класса или экземпляром класса из кортежа.
        # В случае если является, функция возвращает True,
        # если не является — False.
        print("квадрат=",figure.get_area_square())
    else:
        print("прямоугольник=",figure.get_area())
