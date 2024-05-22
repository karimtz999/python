from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Extract feature data (X) and target labels (y)
X = iris['data']
y = iris['target']

# Display the first 5 rows of features and target labels
print("First 5 rows of feature data (X):")
print(X[:5])

print("\nFirst 5 target labels (y):")
print(y[:5])
