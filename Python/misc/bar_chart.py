# Importing the Matplotlib library for plotting
import matplotlib.pyplot as plt

# Defining the data for the bar chart
categories = ['A', 'B', 'C', 'D']  # Categories for the x-axis
values = [15, 30, 45, 10]  # Heights of the bars corresponding to each category

# Creating the bar chart
plt.bar(categories, values, color='skyblue', edgecolor='black')

# Adding labels and a title
plt.xlabel('Categories')  # Label for the x-axis
plt.ylabel('Values')      # Label for the y-axis
plt.title('Bar Chart Example')  # Title of the chart

# Displaying the chart
plt.show()
