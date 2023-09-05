import psutil
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Prints CPU usage and other stats to console
def cpu_usage(label):
    # fetch current process
    application = psutil.Process(os.getpid())
    print("")
    print(f"--- {label} ---")
    print(f"CPU Usage: {psutil.cpu_percent(interval=None)}")
    print(f"Memory Statistics: {application.memory_info()}")
    print(f"Disk Usage: {psutil.disk_usage('/')}")
    print("\n")


# store CPU usage
cpu_stats = []


# Appends CPU usage to cpu_stats list
def usage_history():
    cpu_percent = psutil.cpu_percent()
    cpu_stats.append(cpu_percent)


# Graphs CPU usage
def graph_cpu_stats():
    df = pd.DataFrame(cpu_stats, columns=["CPU Percentage"])
    df['Type'] = ['Multithreading' if i < len(cpu_stats) / 2 else 'Multiprocessor' for i in
                  range(len(cpu_stats))]

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x=df.index, y="CPU Percentage", hue="Type")
    plt.title("CPU Usage Comparison")
    plt.ylabel("CPU Percentage")
    plt.xlabel("Time (Seconds since start)")
    plt.show()
