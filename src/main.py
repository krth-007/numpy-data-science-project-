import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [25, 60, 12],
    [30, 65, 10],
    [28, 70, 14],
    [32, 55, 9]
])

print("Dataset:\n", data)

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

print("Column Mean:", np.mean(data, axis=0))

view_array = data.view()
copy_array = data.copy()

# Indexing
print("Indexed element:", data[1,2])


print("First two rows:\n", data[0:2])

humidity = data[:,1]
print("Humidity column:", humidity)

subset = data[data[:,0] > 28]
print("Subset where temperature > 28:\n", subset)

flat_array = data.flatten()
print("Flattened array:", flat_array)

flat2 = data.ravel()

reshaped = data.reshape(2,6)
print("Reshaped array:\n", reshaped)

temperature = data[:,0]

plt.plot(temperature)
plt.title("Temperature Distribution")
plt.xlabel("Observation Index")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()
