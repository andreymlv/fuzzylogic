
import matplotlib.pyplot as plt
import figures as fg



def print_trapezoid(args):

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


def main():
    args = [2, 10, 6]
    x = list()
    triangles = list()

    fig, ax = plt.subplots()



    for i in range(int(input("Enter number of X's => "))):
        x_current = float(input("Enter x => "))
        x.append(x_current)
        triangles.append(fg.Triangle(*args, x[i]))
    
    for i in range(len(triangles)):
        coords = triangles[i].get_coords()
        
        for j in range(len(coords[0])):
            coords[0][j] += triangles[i].a * i

        ax.plot(coords[0], coords[1])


    # print_trapezoid(take_input())
    plt.show()


if __name__ == "__main__":
    main()
