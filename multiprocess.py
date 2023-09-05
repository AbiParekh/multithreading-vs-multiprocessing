import multiprocessing
from measure import cpu_usage


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def worker(num):
    print(f"Factorial of {num}: {factorial(num)}")


def multiProcess(n):
    processes = []
    for i in range(1, n + 1):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    cpu_usage("Multiprocessing")


if __name__ == '__main__':
    multiProcess(5)
