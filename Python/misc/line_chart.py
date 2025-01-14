# Importing the Matplotlib library for plotting
import matplotlib.pyplot as plt

# Defining the data for the line chart
x = [1, 2, 3, 4, 5]  # Values for the x-axis
y = [2, 4, 1, 8, 7]  # Corresponding values for the y-axis

# Creating the line chart
plt.plot(x, y, marker='o', linestyle='-', color='purple', label='Line 1')

# Adding labels and a title
plt.xlabel('X-axis')  # Label for the x-axis
plt.ylabel('Y-axis')  # Label for the y-axis
plt.title('Line Chart Example')  # Title of the chart

# Adding a legend
plt.legend()

# Displaying the chart
plt.show()
