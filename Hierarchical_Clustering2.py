import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Generate random data points
np.random.seed(42)
x = np.random.rand(10) * 10
y = np.random.rand(10) * 10
data = list(zip(x, y))

# Compute linkage data
linkage_data = linkage(data, method='ward', metric='euclidean')

# Create the dendrogram
dendrogram(linkage_data)

# Save the plot as an image
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
