
import matplotlib.pyplot as plt


def triangle(upper, lower, peak, x):
    u = 0
    if ((x >= lower) and (x <= peak)):
        u = 1 - ((peak - x) / (peak - lower))
        return u
    if ((x >= peak) and (x <= upper)):
        u = 1 - ((x - peak) / (upper - peak))
        return u
    return u


def trapezoid(upper, lower, peak_lower, peak_upper, x):
    u = 0
    if ((x >= lower) and (x <= peak_lower)):
        u = 1 - ((peak_lower - x) / (peak_lower - lower))
        return u
    if (x >= peak_lower) and (x <= peak_upper):
        u = 1
        return u
    if ((x >= peak_upper) and (x <= upper)):
        u = 1 - ((x - peak_upper) / (upper - peak_upper))
        return u
    return u


def print_triangle(args):

    if args[0] == 1:
        pass
    elif args[0] == 2:
        print_trapezoid(args)
    else:
        return

    lower = args[1]
    upper = args[2]
    a = upper - lower
    peak = args[3]
    x = args[-1]
    len_of_x = len(x)

    for i in range(len_of_x):

        print(x[i])

        u = triangle(upper, lower, peak, x[i])

        x_list = [lower+a*i, upper-x[i]+lower+a*i, x[i]+a*i, upper+a*i]
        y_list = [0, u, u, 0]

        if (u == 1):
            plt.plot([lower+a*i, x[i]+a*i, upper+a*i], [0, 1, 0])
        else:
            plt.plot(sorted(x_list), y_list)


def print_trapezoid(args):

    if args[0] == 2:
        pass
    elif args[0] == 1:
        print_triangle(args)
    else:
        return

    lower = args[1]
    upper = args[2]
    a = upper - lower
    peak1 = args[3]
    peak2 = args[4]
    x = args[-1]
    len_of_x = len(x)

    for i in range(len_of_x):

        u = trapezoid(upper, lower, peak1, peak2, x[i])

        x_list = [lower+a*i, upper-x[i]+lower+a*i, x[i]+a*i, upper+a*i]
        y_list = [0, u, u, 0]

        if (u == 1):
            plt.plot([lower+a*i, peak1+a*i, peak2 +
                      a*i, upper+a*i], [0, 1, 1, 0])
        else:
            plt.plot(sorted(x_list), y_list)


def take_input():

    flag = int(input(
        "What method do you want to solve? (triangular or trapezoidal) (1 or 2) --> "))
    lower = float(input("Enter lower value --> "))
    upper = float(input("Enter upper value  --> "))

    number_of_vars = int(input("Enter the number of variables --> "))
    array_with_crisp = list()
    for value in range(number_of_vars):
        value = float(
            input("Enter your " + str(value + 1) + " scrisp value --> "))
        array_with_crisp.append(value)

    if flag == 1:
        peak = float(input("Enter yours peak value --> "))
        return [flag, lower, upper, peak, array_with_crisp]
    elif flag == 2:
        peak1 = float(input("Enter yours first peak value --> "))
        peak2 = float(input("Enter yours second peak value --> "))
        return [flag, lower, upper, peak1, peak2, array_with_crisp]
    else:
        return 1


def main():
    print_trapezoid(take_input())
    plt.show()


if __name__ == "__main__":
    main()
