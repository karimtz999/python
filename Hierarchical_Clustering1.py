import matplotlib.pyplot as plt

# Sample data for x and y coordinates
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
plt.plot(x, y)

# Save the plot to a file instead of showing it
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
