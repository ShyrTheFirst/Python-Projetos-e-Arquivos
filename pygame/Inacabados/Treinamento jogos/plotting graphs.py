import matplotlib.pyplot as plt
 
# defining labels
activities = ['eat', 'sleep', 'work', 'play']
 
# portion covered by each label
slices = [10, 10, 50, 30]
 
# color for each label
colors = ['r', 'y', 'g', 'b']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True, explode = (0.1, 0.1, 0.1, 0.1),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()
