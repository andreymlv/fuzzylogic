
from math import e
from math import pow
from math import sqrt


class FuzzySet():
    def __init__(self, name):
        """
        name - название множества входа/выхода
        """
        self.name = name

    def trapmf(self, x, a, b, c, d):
        """
        Трапециевидная функция принадлежности
        """
        result = list()

        for n in x:
            if (n < a) or (n > d):
                continue
            if b == a:
                b += 0.1
            elif d == c:
                c -= 0.1
            u = max(min((n-a)/(b-a), 1, (d-n)/(d-c)), 0)
            result.append(u)

        return result

    def trimf(self, x, a, b, c):
        """
        Треугольная функция принадлежности
        """
        result = list()

        for n in x:
            if (n < a) or (n > c):
                continue
            if b == a:
                b += 0.1
            elif c == b:
                b -= 0.1
            u = max(min((n-a)/(b-a), (c-n)/(c-b)), 0)
            result.append(u)

        return result

    def gaussmf(self, x, p, c):
        """
        Гауссовская функция принадлежности
        """
        result = list()

        for n in x:
            if (pow(e, -pow((n-c), 2)/(2*pow(p, 2))) == 0):
                continue
            u = pow(e, -pow((n-c), 2)/(2*pow(p, 2)))
            result.append(u)
        return result

    def negation(self, fuzzy_set):
        """
        !A
        """
        result = list()

        for i in fuzzy_set:
            result.append(1-i)

        return result

    def conjugation(self, fuzzy_set1, fuzzy_set2):
        """
        Конъюнкция
        A^B (AND)
        """
        return min(fuzzy_set1, fuzzy_set2)

    def disjunction(self, fuzzy_set1, fuzzy_set2):
        """
        Дизъюнкция
        AvB (OR)
        """
        return max(fuzzy_set1, fuzzy_set2)

    def concentrasion(self, fuzzy_set):
        """
        Концентрация
        A^2
        """
        result = list()

        for i in fuzzy_set:
            result.append(pow(i, 2))

        return result

    def dilatation(self, fuzzy_set):
        """
        Дилатация
        sqrt(A)
        """
        result = list()

        for i in fuzzy_set:
            result.append(sqrt(i))

        return result

    def activation(self, fuzzy_set, func, args):
        """
        Активация
        """
        result = list()
        u = func(*args)

        result.append(min(fuzzy_set, u))
        result.append(args[1])
        result.append(args[2])

        return result

    def accumulation(self, a1, a2):
        """
        Активация
        """
        return a1 if a1[0] > a2[0] else a2

    def __str__(self):
        """
        Если объект строка, то возвращать имя множества
        """
        return self.name
