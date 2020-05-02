"""
Необходимо скачать Python с официального сайта для вашей ОС.
Необходимо скачать библиотеку matplotlib.

Команда в CMD для установки matplotlib (только после установки Python):

pip install matplotlib

Для запуска программы необходимо ввести в CMD команду (только после установки Python и библиотеки):

python main.py


Авторы - Andrey&Sava
"""

# используем библиотеку для графиков
import matplotlib.pyplot as plt
# используем наш модуль для функций принадлежности
import figures as fg

# Главная функия


def main():
    """
    args - значения для функции принадлежности.
    В данном случае для треугольника.

    [<MINIMAL_VALUE>, <MAXIMAL_VALUE>, <PEAK_VALUE>]
    """
    args = [2, 10, 6]
    # x - хранит в себе список значений параметра, степень нечёткого равенства мы вычисляем
    x = list()
    # triangles - хранит в себе список объектов "треугольников"
    triangles = list()

    # иницилизация для графиков
    fig, ax = plt.subplots()

    # этот цикл заполняет список 'x' и сзаполняет список треугольников с пользовательским параметром
    for i in range(int(input("Enter number of X's => "))):
        # x_current - хранит в себе текущее пользовательское значение параметра
        x_current = float(input("Enter x => "))
        # добавляем в список 'x' <- x_current
        x.append(x_current)
        # добавляет в список 'triangles' <- наш треугольник со значениями для функции принадлежности
        triangles.append(fg.Triangle(*args, x[i]))

    for i in range(len(triangles)):
        # coords - хранит в себе координаты для текущей функции
        coords = triangles[i].get_coords()

        # Добавляем шаг для каждого подграфика
        for j in range(len(coords[0])):
            # данная операция делает слияние "напополам" с графиками
            coords[0][j] += ((triangles[i].upper - triangles[i].lower)/2)*i
        # добавляем подграфик в основной график
        triangles[i].make_plot(coords[0], coords[1], ax)

    # Показываем график
    plt.show()


# если файл хранит в себе главную функцию main, то выполняем эту функцию
if __name__ == "__main__":
    main()
