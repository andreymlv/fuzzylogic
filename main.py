"""
Необходимо скачать Python с официального сайта для вашей ОС.
Необходимо скачать библиотеку matplotlib.

Команда в CMD для установки matplotlib (только после установки Python):

pip install matplotlib

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

    # 
    for i in range(int(input("Enter number of X's => "))):
        x_current = float(input("Enter x => "))
        x.append(x_current)
        triangles.append(fg.Triangle(*args, x[i]))

    for i in range(len(triangles)):
        # coords - хранит в себе координаты для текущей функции
        coords = triangles[i].get_coords()

        # Добавляем шаг для каждого подграфика
        for j in range(len(coords[0])):
            coords[0][j] += ((triangles[i].upper - triangles[i].lower)/2)*i
        # добавляем подграфик в основной график
        triangles[i].make_plot(coords[0], coords[1], ax)
    
    # Показываем график
    plt.show()


if __name__ == "__main__":
    main()
