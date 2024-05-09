import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 8, 1, 10, 5]

# Create a bar chart
plt.bar(categories, values)

# Save the plot to a file instead of showing it
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
