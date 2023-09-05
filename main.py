from multithread import multiThreading
from multiprocess import multiProcess
from measure import graph_cpu_stats

if __name__ == '__main__':
    # Run both versions
    multiThreading(5)
    multiProcess(5)

    # Visualize measurements
    graph_cpu_stats()
