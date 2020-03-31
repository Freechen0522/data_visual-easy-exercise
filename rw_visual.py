import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c = point_numbers,cmap = plt.cm.Blues,
                edgecolor = 'none', s = 15)

    plt.scatter(0,0,c = 'green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none',
                s = 100)

    plt.scatter(rw.x_values[-1], rw.y_values[-1],c = 'red', edgecolors = 'none',
                s = 100)

    plt.axes().getxaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.figure(figsize = (10, 6))
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break