import numpy as np

# Create a random (1, 1000, 3) numpy array
random_array_1 = np.random.rand(1, 1000, 1)
random_array_1 = (random_array_1 - np.min(random_array_1)) / (np.max(random_array_1) - np.min(random_array_1))
random_array_1 = np.repeat(random_array_1, 3, axis=2)

# Create a random (48, 1000, 3) numpy array with the third dimension having the same values
random_array_2 = np.random.rand(48, 1000, 1)
random_array_2 = (random_array_2 - np.min(random_array_2)) / (np.max(random_array_2) - np.min(random_array_2))
random_array_2 = np.repeat(random_array_2, 3, axis=2)

# Scale the arrays to 0-255 and convert the type to integer
random_array_1 = (random_array_1 * 255).astype(np.uint8)
random_array_2 = (random_array_2 * 255).astype(np.uint8)

# Print the arrays
print(random_array_1.shape)
print(random_array_2.shape)
assert random_array_2[:, :, 0].all() == random_array_2[:, :, 1].all() == random_array_2[:, :, 2].all()
assert random_array_1[:, :, 0].all() == random_array_1[:, :, 1].all() == random_array_1[:, :, 2].all()


from PIL import Image

# Resize the random_array_1 to 224x224x3
resized_array_1 = np.array(Image.fromarray(random_array_1).resize((224, 224), resample = Image.Resampling.NEAREST, reducing_gap = None))
reversed_array_1 = np.array(Image.fromarray(resized_array_1).resize((1, 1000), resample = Image.Resampling.NEAREST, reducing_gap = None))
# Resize the random_array_2 to 224x224x3
resized_array_2 = np.array(Image.fromarray(random_array_2).resize((224, 224), resample = Image.Resampling.NEAREST, reducing_gap = None))
reversed_array_2 = np.array(Image.fromarray(resized_array_2).resize((48, 1000), resample = Image.Resampling.NEAREST, reducing_gap = None))


print(np.abs(random_array_1 - reversed_array_1).max())
# This returns 255
print(np.all(random_array == reversed_array_1))
# This returns False

# I tried this with resizing with multiples of 224 as the original size and still big absolute difference. 
