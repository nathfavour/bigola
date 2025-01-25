import time
import matplotlib.pyplot as plt

# using the for loop method
def square_loop(n):
    """Return a list of the first n square numbers using a loop."""
    square_nums = []
    for i in range(n):
        square_nums.append(i**2)
    return square_nums

# using the list comprehension method
def square_comprehension(n):
    """Return a list of the first n square numbers using a list comprehension."""
    return [i**2 for i in range(n)]
    

def measure_runtimes(sizes):
    """Measure runtimes of both functions for a range of sizes."""
    loop_times = []
    comp_times = []

    for size in sizes:
        start = time.time()
        square_loop(size)
        loop_times.append(time.time() - start)

        start = time.time()
        square_comprehension(size)
        comp_times.append(time.time() - start)

    return loop_times, comp_times


def plot_runtimes(sizes, loop_times, comp_times):
    """Plot the runtime of the two functions using matplotlib."""
    plt.plot(sizes, loop_times, label='Square Loop')
    plt.plot(sizes, comp_times, label='Square Comprehension')
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    plt.title('Runtime Comparison')
    plt.legend()
    plt.show()


def main():
    """Run sample demonstration of the square functions and plotting"""
    sizes = [10, 100, 1000, 5000, 10000]
    loop_times, comp_times = measure_runtimes(sizes)
    plot_runtimes(sizes, loop_times, comp_times)

if __name__ == "__main__":
    main()
