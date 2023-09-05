import threading
from measure import cpu_usage


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def worker(num):
    print(f"Factorial of {num}: {factorial(num)}")


def multiThreading(n):
    threads = []
    for i in range(1, n + 1):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    cpu_usage("Multithreading")


if __name__ == '__main__':
    multiThreading(5)
