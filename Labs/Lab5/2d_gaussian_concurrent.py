import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor, as_completed

STEP = .001

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
    plt.figure()
    plt.imshow(z.T, origin='lower')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"{z.shape} points")
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

    # Determine quadrant label based on position
    if xmax <= 0 and ymin >= 0:
        quadrant = 'top_left'
    elif xmin >= 0 and ymin >= 0:
        quadrant = 'top_right'
    elif xmax <= 0 and ymax <= 0:
        quadrant = 'bottom_left'
    else:  # xmin >= 0 and ymax <= 0
        quadrant = 'bottom_right'
    
    plot(ZZ)
    
    return (quadrant, ZZ)


if __name__ == "__main__":
    """
    Define the parameters for the functions and calculate the time elapsed for running this script
    """
    start = time.time()
    xmin = int(sys.argv[1])
    xmax = int(sys.argv[2])
    ymin = int(sys.argv[3])
    ymax = int(sys.argv[4])
    xrange = (xmax-xmin)

    # main(-2, 2, -2, 2)
    max_workers = int(sys.argv[5])
    step = int((xrange / max_workers)*2)

    # dictionary to store quadrant results
    results = {}

    quadrant_bounds = {
        'top_left':     (xmin, 0, 0, ymax),
        'top_right':    (0, xmax, 0, ymax),
        'bottom_left':  (xmin, 0, ymin, 0),
        'bottom_right': (0, xmax, ymin, 0)
    }

    with ProcessPoolExecutor(max_workers) as executor:
        futures = {executor.submit(main, *bounds): label 
                   for label, bounds in quadrant_bounds.items()}
        
        for future in as_completed(futures):
            quadrant, data = future.result()
            results[quadrant] = data

    # stitch quadrants together     
    top_row = np.hstack([results['bottom_left'], results['top_left']])
    bottom_row = np.hstack([results['bottom_right'], results['top_right']])
    full_array = np.vstack([top_row, bottom_row])

    # plot 
    plt.figure(figsize=(8, 8))
    plt.imshow(full_array.T, origin = 'lower')
    plt.xlabel("X"); plt.ylabel("Y"); plt.title(f"{full_array.shape} points")
    plt.gca().set_aspect(1)
    plt.show()

    elapsed = time.time() - start
    print(f"Elapsed Time: {elapsed}s")