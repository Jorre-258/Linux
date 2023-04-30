import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
sqaures = [1, 4, 9, 16, 25]
plt.plot(input_values, sqaures, linewidth=5)

#set chart title and label axes
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# set size  of tick labels
plt.tick_params(axis='both', labelsize=14)

# show the plot
plt.show()