

class Triangle():
    """
    Этот класс используется для нахождения степени нечёткого равенства 
    методом треугольника
    """

    def __init__(self, lower, upper, peak, x):
        """
        Иницилизация объекта
        lower - минимальное значение параметра
        upper - максимальное значение параметра
        peak - среднее значение параметра
        x - значение параметра заданное пользователем
        """
        self.lower = lower
        self.upper = upper
        self. peak = peak
        self.x = x
        #степень нечёткого равенства треугольника
        self.u = self.mftriangle()

    def mftriangle(self):
        #нахождение степени нечёткого равенства методом треугольника, по стационарной формуле
        u = 0
        if ((self.x >= self.lower) and (self.x <= self.peak)):
            u = 1 - ((self.peak - self.x) / (self.peak - self.lower))
            return u
        if ((self.x >= self.peak) and (self.x <= self.upper)):
            u = 1 - ((self.x - self.peak) / (self.upper - self.peak))
            return u
        return u

    def get_coords(self):
        """
        Функция генерирования координат на основе найденой 
        степени нечёткого равенства
        """
        #выводим степень нечёткого равенства 
        print(self.u)
        """
        здесь в зависимости от полученной степени нечёткого равенства происходит выбор
        координат для нарисования графика параметра
        """
        if (self.u != 1.0):
        #сортируем значения коопдинат, для рисования правильной функции
            x_list = sorted(
                [self.lower, self.lower+self.upper-self.x, self.x, self.upper])
            y_list = [0, self.u, self.u, 0]
        else:
            x_list = sorted([self.lower, self.x, self.upper])
            y_list = [0, self.u, 0]
       #список, который хранит в себе значения координат функции
        coords = list()
        coords.append(x_list)
        coords.append(y_list)

        return coords

    def make_plot(self, ox, oy, ax):
        """Создание графика нечёткого равенства"""
        ax.plot(sorted(ox), oy)


class Trapezoid():
    """
    Этот класс используется для нахождения степени нечёткого равенства 
    методом трапеции
    """

    def __init__(self, lower, upper, first_peak, second_peak, x):
       """
        Иницилизация объекта
        lower - минимальное значение параметра
        upper - максимальное значение параметра
        first_peak - 1-ое среднее значение параметра
        second_peak - 2-ое среднее значение параметра
        x - значение параметра заданное пользователем
        """
        self.lower = lower
        self.upper = upper
        self.first_peak = first_peak
        self.second_peak = second_peak
        self.x = x
        #степень нечёткого равенства трапеции
        self.u = self.mftrapezoid()

    def mftrapezoid(self):
        #нахождение степени нечёткого равенства методом трапеции, по стационарной формуле
        u = 0
        if ((self.x >= self.lower) and (self.x <= self.first_peak)):
            u = 1 - ((self.first_peak - self.x) /
                     (self.first_peak - self.lower))
            return u
        if (self.x >= self.first_peak) and (self.x <= self.second_peak):
            u = 1
            return u
        if ((self.x >= self.second_peak) and (self.x <= self.upper)):
            u = 1 - ((self.x - self.second_peak) /
                     (self.upper - self.second_peak))
            return u
        return u

    def get_coords(self):
        """
        Функция генерирования координат на основе найденой 
        степени нечёткого равенства
        """
        #выводим степень нечёткого равенства
        print(self.u)
        #сортируем значения коопдинат, для рисования правильной функции
        x_list = sorted([self.lower, self.lower+self.upper -
                         self.x, self.x, self.upper])
        y_list = [0, self.u, self.u, 0]
        #список, который хранит в себе значения координат функции
        coords = list()
        coords.append(x_list)
        coords.append(y_list)

        return coords

    def make_plot(self, ox, oy, ax):
        """Создание графика нечёткого равенства"""
        ax.plot(sorted(ox), oy)
