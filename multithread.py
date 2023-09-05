import threading
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


# Initiate multithreading on the simulation
def multiThreading(n):
    threads = []
    for i in range(1, n + 1):
        t = threading.Thread(target=compute, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    cpu_usage("Multithreading")


if __name__ == '__main__':
    multiThreading(5)
