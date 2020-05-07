
from figures import FuzzySet


def main():
    """
    1. number of inputs/outputs
    1.1. how many input variables do you want?
    1.2. how many output variables do you want?

    2. configure inputs/outputs (range of separate i/o, name of each i/o, params of each i/o)
    2.1 input_1 what a type of mf do you want and how enter number of mfs
    ...
    2.1 input_n what a type of mf do you want and how enter number of mfs
    2.2 output_1 what a type of mf do you want and how enter number of mfs
    ...
    2.2 output_m what a type of mf do you want and how enter number of mfs

    3. configure rules

    4. print charts and some info
    """
    
    # i - счётчик
    i = 0
    # n - максимальный диапазон
    n = 30
    # x - список значений для функции принадлежности
    x = list()

    """
    entrances = list()
    exits = list()
    """
    
    # Заполнение x значениями
    while len(x) <= n*10:
        x.append(i)
        i += 0.1
    
    """
    for i in range(int(input("How many entrances = "))):
        entrances.append(list())  # 3

    for i in range(int(input("How many exits = "))):
        exits.append(list())

    for entry in entrances:
        for index in range(int(input("How many mfs in " + str(entrances.index(entry)+1) + " input = "))):
            if input("trapmf? - ") == "y":
                entry.append(FuzzySet(input("Name of mf - ")).trapmf(x, float(input("Enter a = ")),
                                                                     float(
                    input("Enter b = ")),
                    float(
                    input("Enter c = ")),
                    float(input("Enter d = "))))
            elif input("trimf? - ") == "y":
                entry.append(FuzzySet(input("Name of mf - ")).trimf(x, float(input("Enter a = ")),
                                                                    float(
                    input("Enter b = ")),
                    float(input("Enter c = "))))
            elif input("gaussmf? - ") == "y":
                entry.append(FuzzySet(input("Name of mf - ")).gaussmf(x, float(input("Enter p = ")),
                                                                      float(input("Enter c = "))))
            else:
                print("Error")

    for out in exits:
        for index in range(int(input("How many mfs in " + str(exits.index(entry)+1) + " output = "))):
            if input("trapmf? - ") == "y":
                out.append(FuzzySet(input("Name of mf - ")).trapmf(x, float(input("Enter a = ")),
                                                                   float(
                    input("Enter b = ")),
                    float(
                    input("Enter c = ")),
                    float(input("Enter d = "))))
            elif input("trimf? - ") == "y":
                out.append(FuzzySet(input("Name of mf - ")).trimf(x, float(input("Enter a = ")),
                                                                  float(
                    input("Enter b = ")),
                    float(input("Enter c = "))))
            elif input("gaussmf? - ") == "y":
                out.append(FuzzySet(input("Name of mf - ")).gaussmf(x, float(input("Enter p = ")),
                                                                    float(input("Enter c = "))))
            else:
                print("Error")
    
    print(set(entrances[0][1]) & set(exits[0][1]))
    """
    
    # Вход №1 Сервис
    service = [FuzzySet("poor").gaussmf(x, 1, 0.5),
               FuzzySet("good").gaussmf(x, 2, 5),
               FuzzySet("excellent").gaussmf(x, 1, 9.5)]
    
    # Вход №2 Еда
    food = [FuzzySet("rancid").trapmf(x, 0, 0, 1, 3),
            FuzzySet("delicious").trapmf(x, 7, 8, 10, 10)]

    # Выход №1 Чаевые
    tip = [FuzzySet("cheap").trimf(x, 0, 5, 10),
           FuzzySet("average").trimf(x, 10, 15, 20),
           FuzzySet("generous").trimf(x, 20, 25, 30)]

    # rules - лингвистические переменные (в данном случае находим степень нечётного равентва)
    rules = list()
    rules.append((set(service[0]) | set(food[0])) & set(tip[0]))
    rules.append((set(service[1])) & set(tip[1]))
    rules.append((set(service[2]) | set(food[1])) & set(tip[2]))

    # Вывод
    print(service)
    print()
    print()
    print()
    print()
    print(food)
    print()
    print()
    print()
    print()
    print(tip)
    print()
    print()
    print()
    print()
    print(rules)
    


if __name__ == "__main__":
    main()
