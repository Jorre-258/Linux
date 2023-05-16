import pygal
from die import Die

# Create a D6

die = Die()

# Make some rolls and store them in a list
results = []
for roll_number in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist._y_title = "Frequency of result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual_1.svg')
print(frequencies)