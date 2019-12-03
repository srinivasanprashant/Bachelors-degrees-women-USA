import pandas as pd
import matplotlib.pyplot as plt


women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

# fig, ax = plt.subplots()
# ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
# ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
# # customize the appearance of the ticks
# ax.tick_params(bottom="off", top="off", left="off", right="off")
# ax.set_title('Percentage of Biology Degrees Awarded By Gender')
# ax.legend(loc="upper right")

# From the plot, we can tell that Biology degrees increased steadily from 1970 and peaked in the early 2000's.
# We can also tell that the percentage has stayed above 50% since around 1987.

# Now let's generate line charts for four STEM degree categories on a grid to encourage comparison
# major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
# fig = plt.figure(figsize=(12, 10))
#
# for sp in range(0,4):
#     ax = fig.add_subplot(2,2,sp+1)
#     ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
#     ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
#     # Add your code here.
#     # Set the x-axis limit to range from 1968 to 2011
#     ax.set_xlim(1968, 2011)
#     # Set the y-axis limit to range from 0 to 100
#     ax.set_ylim(0, 100)
#     # Hide all of the spines and tick marks
#     ax.tick_params(bottom="off", top="off", left="off", right="off")
#     ax.spines["right"].set_visible(False)
#     ax.spines["bottom"].set_visible(False)
#     ax.spines["top"].set_visible(False)
#     ax.spines["left"].set_visible(False)
#     ax.set_title(major_cats[sp])
#
# # Calling pyplot.legend() here will add the legend to the last subplot that was created.
# plt.legend(loc='upper right')
# plt.suptitle('Percentage of STEM Degrees Awarded By Gender')

# plt.show()

# Computer Science and Engineering have big gender gaps while the gap in Biology and Math and Statistics is
# quite small. In addition, the first two degree categories are dominated by men while the latter degree
# categories are much more balanced.

# Now we'll focus on customizing colors, line widths, layout, and annotations to improve the ability
# for a viewer to extract insights from the charts.

# order the charts by decreasing ending gender gap using list populated in that order
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
# Make plots more color-blind friendly using colors from color-blind friendly palette
cb_dark_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)

fig = plt.figure(figsize=(18, 4))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    # add text annotations to plot
    if sp == 0:
        # Annotating using Axes.text(x coordinate, y coordinate, string of text)
        ax.text(2005, 87, "Men")
        ax.text(2002, 8, "Women")
    elif sp == 5:
        ax.text(2005, 62, "Men")
        ax.text(2001, 35, "Women")
legend = ax.legend()
legend.remove()

plt.suptitle('Percentage of STEM Degrees Awarded By Gender')

# Next step is to build a bigger plot.
# Because there are seventeen degrees that we need to generate line charts for, we'll use a subplot
# grid layout of 6 rows by 3 columns. We can then group the degrees into STEM, liberal arts, and other

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']
# Make plots more color-blind friendly using colors from color-blind friendly palette
cb_dark_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)

fig = plt.figure(figsize=(16, 20))

for sp in range(0,6):
    ax = fig.add_subplot(6,3,(3*sp)+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    # add text annotations to plot
    if sp == 0:
        # Annotating using Axes.text(x coordinate, y coordinate, string of text)
        ax.text(2005, 85, "Women")
        ax.text(2005, 10, "Men")
    elif sp == 5:
        ax.text(2005, 87, "Men")
        ax.text(2005, 7, "Women")

for sp in range(0,5):
    ax = fig.add_subplot(6,3,(3*sp)+2)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    # add text annotations to plot
    if sp == 0:
        # Annotating using Axes.text(x coordinate, y coordinate, string of text)
        ax.text(2005, 78, "Women")
        ax.text(2005, 18, "Men")

for sp in range(0,6):
    ax = fig.add_subplot(6,3,(3*sp)+3)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    # add text annotations to plot
    if sp == 0:
        # Annotating using Axes.text(x coordinate, y coordinate, string of text)
        ax.text(2005, 90, "Women")
        ax.text(2005, 5, "Men")
    elif sp == 5:
        ax.text(2005, 62, "Men")
        ax.text(2005, 30, "Women")

legend = ax.legend()
legend.remove()

#plt.suptitle('Percentage of STEM Degrees Awarded By Gender')

plt.show()
