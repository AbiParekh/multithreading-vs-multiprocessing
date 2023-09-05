import psutil
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def cpu_usage(label):
    application = psutil.Process(os.getpid())
    print("")
    print(f"--- {label} ---")
    print(f"CPU Percent: {psutil.cpu_percent(interval=None)}")
    print(f"Memory Info: {application.memory_info()}")
    print(f"Disk Usage: {psutil.disk_usage('/')}")
    print("\n")


cpu_stats = []


def usage_history():
    cpu_percent = psutil.disk_usage()
    cpu_stats.append(cpu_percent)


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
