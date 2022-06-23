# To calculate average height and standard deviation

import math  # Importing math module


def mean_n_std(data):
    n = len(data)
    mean = sum(data) / n
    std_dev = math.sqrt(sum([(i - mean) ** 2 for i in data]) / n)
    return mean, std_dev


if __name__ == "__main__":
    heights = [4.5, 4.9, 4.8, 5.3, 5.7, 5.0, 4.8, 5.2, 4.7, 5.1, 4.4, 4.9]  # Making list of heights

    print(f"Mean, Standard Deviation: {mean_n_std(heights)}")
