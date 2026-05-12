import time
import numpy as np
import matplotlib.pyplot as plt

STEP = .0005

def gaussian2D(x, y, sigma):
    """
    calculate the gaussian function when given x, y, and sigma values.
    
    x and y are input coordinates 
    sigma represents a constant needed to calculate the gaussian function 
    """
    return (1/(2*np.pi*sigma**2))*np.exp(-1*(x**2+y**2)/(2*sigma**2))

def plot(z):
    """
    plot the gaussian function for each x and y coordinate pair, stored in z 
    """
    plt.imshow(z.T)
    plt.gca().invert_yaxis()  # flip axes to get imshow to plot representatively
    plt.xlabel("X"); plt.ylabel("Y"); plt.title(f"{z.shape} points")
    plt.gca().set_aspect(1)

def main(xmin, xmax, ymin, ymax, sigma=1):
    """
    Plot the gaussian values for each point given axes bounds and a sigma value
    """
    X = np.arange(float(xmin), float(xmax), STEP)
    Y = np.arange(float(ymin), float(ymax), STEP)
    Z = []  # 1D array
    for x in X:
        for y in Y:
            Z.append(gaussian2D(x, y, sigma))
    ZZ = np.array(Z).reshape(len(X), len(Y))  # 2D array
    plot(ZZ)
    return ZZ

if __name__ == "__main__":
    """
    Define the parameters for the functions and calculate the time elapsed for running this script
    """
    start = time.time()
    main(-2, 2, -2, 2)
    elapsed = time.time() - start
    print(f"Elapsed Time: {elapsed}s")
    plt.show()