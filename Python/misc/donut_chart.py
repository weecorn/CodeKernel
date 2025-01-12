# Importing the Matplotlib library for plotting
import matplotlib.pyplot as plt

# Defining the data for the pie chart
sizes = [15, 30, 45, 10]  # Sizes of the pie slices
labels = ['A', 'B', 'C', 'D']  # Labels corresponding to each slice

# Creating a pie chart with the given sizes and labels
# 'autopct' adds percentage values to each slice
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Creating a white circle to transform the pie chart into a donut chart
circle = plt.Circle((0, 0), 0.8, color='white')  # (0,0) is the center; 0.8 is the radius
plt.gca().add_artist(circle)  # Adding the circle to the current axes

# Adding a title to the chart
plt.title('Donut Chart')

# Displaying the chart
plt.show()
