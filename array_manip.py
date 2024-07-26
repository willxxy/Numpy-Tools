import numpy as np

# Original signal
signal = np.arange(24).reshape(6, 4)
print("Original signal (6, 4):\n", signal)

# Reshaping
reshaped_signal = signal.reshape(4, 6)
print("\nReshaped signal (4, 6):\n", reshaped_signal)

# Transposing
transposed_signal = np.transpose(signal, (1, 0))
print("\nTransposed signal (4, 6):\n", transposed_signal)

# Just add anoteher dimension?
data = np.array([[1, 2, 3], [4, 5, 6]])
new_data = np.expand_dims(data, axis=0)
print(new_data.shape)  # Output: (1, 2, 3)

### THESE TWO ARE DIFFERENT
'''
Original signal (6, 4):
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]

Reshaped signal (4, 6):
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

Transposed signal (4, 6):
 [[ 0  4  8 12 16 20]
 [ 1  5  9 13 17 21]
 [ 2  6 10 14 18 22]
 [ 3  7 11 15 19 23]]

'''
