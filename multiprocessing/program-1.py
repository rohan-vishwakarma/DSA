import multiprocessing

def square(n):
    return n * n


if __name__ == '__main__':  # Critical for Windows/macOS to avoid recursion
    numbers = [1, 2, 3, 4, 5]

    # Create a pool of processes (default: CPU cores)
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)

    print("Squares:", results)