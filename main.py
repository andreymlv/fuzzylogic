
import matplotlib.pyplot as plt
import figures as fg

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

        triangles[i].make_plot(coords[0], coords[1], ax)
    
    plt.show()


if __name__ == "__main__":
    main()
