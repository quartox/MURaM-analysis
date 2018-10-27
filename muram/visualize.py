import matplotlib.pyplot as plt
import numpy as np


def display_heights(array, num_slices=4, metadata=None):
    """Display a horizontal slice of data at 10 heights through the 3D array"""
    ny = array.shape[1]
    i = 0
    while i < ny:
        plt.imshow(array[:, i, :])
        if metadata:
            title = f'{metadata} at y index {i} of {ny}'
        else:
            title = f'y index {i} of {ny}'
        plt.title(title)
        plt.show()
        i += int(ny / num_slices)


def plot_vertical_rms(array, metadata=None):
    """Plot the vertical root-mean-square (RMS) of the array."""
    square = np.square(array)
    mean = np.mean(np.mean(square, axis=2), axis=0)
    rms = np.sqrt(mean)
    plt.plot(rms)
    plt.xlabel('vertical index')
    plt.ylabel('RMS')
    if metadata:
        plt.title(metadata)
    plt.show()
