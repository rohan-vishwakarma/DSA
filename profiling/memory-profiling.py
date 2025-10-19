# profiling_demo.py
import time
import random
import cProfile
from memory_profiler import profile

# Function 1: Slow computation
@profile
def compute_squares(n):
    result = []
    for i in range(n):
        result.append(i * i)
        time.sleep(0.0001)   # simulate delay
    return result


# Function 2: Generate random numbers and sort them
@profile
def generate_and_sort(n):
    data = [random.random() for _ in range(n)]
    data.sort()
    return data


def main():
    print("Running compute_squares...")
    squares = compute_squares(1000)

    print("Running generate_and_sort...")
    sorted_data = generate_and_sort(10000)

    print("Computation done!")


if __name__ == "__main__":
    # Run CPU profiling
    cProfile.run("main()", sort="time")
