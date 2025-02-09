import numpy as np

# Generate a random array
a1 = np.random.random(10)
print("Array:", a1)

# Mean, Max, Min, Sum, Standard Deviation, Variance
print("Mean:", a1.mean(),end="\n")
print("Max:", a1.max())
print("Min:", a1.min())
print("Sum:", a1.sum())
print("Standard Deviation:", a1.std())
print("Variance:", a1.var())

# Median and Percentile
print("Median:", np.median(a1))
print("25th Percentile:", np.percentile(a1, 25))

# Mode (manual calculation using np.unique)
values, counts = np.unique(a1, return_counts=True)
max_count_index = np.argmax(counts)
mode_value = values[max_count_index]
print("Mode:", mode_value)