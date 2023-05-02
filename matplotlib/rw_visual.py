import matplotlib.pyplot as plt
from random_walk import RandomWalk

# make a random walk and plot the points
while keep_running := input("Do you want to play again? ") != 'no':
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

    # Emphasize the first and last point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

