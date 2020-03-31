import pygal

from die import Die

# create a D6

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequedcy of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)