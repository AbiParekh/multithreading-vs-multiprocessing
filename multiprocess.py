import multiprocessing
from measure import cpu_usage


# Simulation of a task
def simulate(n):
    if n == 0:
        return 1
    else:
        return n * simulate(n - 1)


# Uses the simulation and prints the result
def compute(num):
    print(f"Recursion of {num}: {simulate(num)}")


# Initiate multiprocessing on the simulation
def multiProcess(n):
    processes = []
    for i in range(1, n + 1):
        p = multiprocessing.Process(target=compute, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    cpu_usage("Multiprocessing")


if __name__ == '__main__':
    multiProcess(5)
