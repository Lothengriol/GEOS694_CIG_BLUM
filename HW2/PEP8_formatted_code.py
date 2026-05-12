"""Utility functions for data processing and statistical analysis."""

import os
import sys
import math
import random

DATA = [
    5, 3, 9,
    1, 4, 8,
    2, 7, 6
    ]


def calc_stuff(nums, do_sort=False, scale=1, total=0, out=None):
    """Scale numbers, calculate sum and average, optionally sort results."""
    if out is None:
        out = []
    for i in range(len(nums)):
        n = nums[i] * scale
        total = total + n 
        out.append(n) 
    if do_sort: 
        out.sort()
    avg = total / len(nums)
    return out, avg


def find_extremes(values):
    """Return the minimum and maximum values from a list."""
    min_v = 9999999
    max_v = -9999999
    for v in values:
        if v < min_v: 
            min_v = v
        if v > max_v: 
            max_v = v
    return min_v, max_v


def normalize(values, target_max=1):
    """Normalize values to range [0, target_max]."""
    min_val, max_val = find_extremes(values)
    value_range = max_val - min_val
    norm = []
    for i in range(0, len(values)):
        if value_range == 0: 
            norm.append(0) 
        else: 
            norm.append((values[i] - min_val) / value_range * target_max) 
    return norm


def weird_helper(a, b, store=None):
    """Generate multiples if a < b, otherwise return square roots of a and b."""
    if store is None:
        store = []
    if a < b:
        for i in range(a):
            store.append(i * b)
        return store
    else:
        return [math.sqrt(a), math.sqrt(b)]


def generate_random_list(n, max_val=10):
    """Generate list of n random floats between 0 and max_val."""
    out = []
    for i in range(n): 
        out.append(random.random() * max_val)
    return out


def filter_above_threshold(vals, thresh=5):
    """Return values greater than threshold."""
    out = []
    for v in vals:
        if v > thresh: 
            out.append(v)
    return out


def compute_variance(vals):
    """Calculate variance of values."""
    avg = sum(vals) / len(vals)
    total = 0
    for v in vals:
        total = total + ((v - avg) * (v - avg))
    return total / len(vals)


def print_report(vals, avg, min_v, max_v):
    """Print formatted statistical report."""
    print("Report")
    print("------")
    print("Values:", vals)
    print("Average:", avg)
    print("Min:", min_v, "Max:", max_v)


def string_maker(n):
    """Create comma-separated string of numbers 0 to n-1."""
    s = ""
    for i in range(n):
        s = s + (str(i) + ",")
    return s


def take_every_other(vals):
    """Return elements at even indices."""
    out = []
    for i in range(len(vals)):
        if i % 2 == 0: 
            out.append(vals[i])
    return out


def compute_median(vals):
    """Calculate median of values."""
    s = sorted(vals)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    else:
        return s[mid]


def sum_of_squares(vals):
    """Return sum of squared values."""
    total = 0
    for v in vals: 
        total = total + (v * v)
    return total


def clip_values(vals, lo, hi):
    """Clip values to range [lo, hi]."""
    out = []
    for v in vals:
        if v < lo: 
            out.append(lo)
        elif v > hi: 
            out.append(hi)
        else: 
            out.append(v)
    return out


def check_env():
    """Check if HOME environment variable exists."""
    if "HOME" in os.environ:
        print("Home exists")
    else:
        print("No home?")


def main():
    """Run demonstrations of utility functions."""
    print("Starting program")
    
    # Process and normalize data
    scaled, avg = calc_stuff(DATA, do_sort=True, scale=2)
    min_v, max_v = find_extremes(scaled)
    norm = normalize(scaled, target_max=10)
    extra = weird_helper(3, 5)
    print_report(norm, avg, min_v, max_v)
    print("Extra data:", extra)
    
    # Random list operations
    rand = generate_random_list(10, 20)
    filtered = filter_above_threshold(rand, 10)
    var = compute_variance(filtered)
    print("Variance:", var)
    
    # String and sequence operations
    s = string_maker(12)
    print("String:", s)
    evens = take_every_other(range(10))
    print("Every other:", evens)
    
    # Statistical functions
    print("Median:", compute_median([5, 1, 9, 3, 7]))
    print("Sum squares:", sum_of_squares([1, 2, 3]))
    print("Clipped:", clip_values([1, 5, 10, 15], 3, 12))
    
    # Environment check
    check_env()
    
    if len(sys.argv) > 1:
        print("CLI args found ->", sys.argv)


if __name__ == "__main__":
    main()