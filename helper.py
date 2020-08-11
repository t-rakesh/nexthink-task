import psutil
import os.path
import pandas as pd

M_CPU_USAGE = 'cpu_usage'
M_PVT_MEMORY = 'private_memory'
M_OPEN_FILES = 'open_files'


def get_associated_pids(name):
    pids = []
    for proc in psutil.process_iter():
        if proc.name() == name:
            pids.append(proc.pid)
    if not pids:
        raise Exception('No such process')
    return pids


def create_files(process_name, pids):
    for pid in pids:
        file_name = f'{process_name}_{pid}.csv'
        if os.path.isfile(file_name):
            os.remove(file_name)
        df = pd.DataFrame(list(), columns=[M_CPU_USAGE, M_PVT_MEMORY, M_OPEN_FILES])
        df.to_csv(file_name, index=False)


def get_metrics(pid):
    metrics = dict()
    try:
        p = psutil.Process(pid)
        cpu_usage = []
        for i in range(5):
            cpu_usage.append(p.cpu_percent(interval=0.1))
        with p.oneshot():
            metrics[M_CPU_USAGE] = float(sum(cpu_usage)/len(cpu_usage))
            metrics[M_PVT_MEMORY] = p.memory_full_info().rss
            metrics[M_OPEN_FILES] = len(p.open_files())
    except psutil.NoSuchProcess:
        print(f"process with id {pid} is not present")
    return metrics


def process_metrics(pname, metrics, path):
    if metrics:
        write_df = pd.DataFrame([metrics])
        write_df.to_csv(path, mode='a', index=False, header=False)
    df = pd.read_csv(path)
    avg_cpu = df[M_CPU_USAGE].mean()
    avg_memory = df[M_PVT_MEMORY].mean()
    avg_ofiles = df[M_OPEN_FILES].mean()
    is_monotonic_increasing = False
    if len(df[M_PVT_MEMORY]) > 1:
        is_monotonic_increasing = df[M_PVT_MEMORY].is_monotonic_increasing
    print(f'{pname}: average [cpu_usage: {avg_cpu}, private_memory: {avg_memory}, open_files: {avg_ofiles}]: memory_usage_increasing: {is_monotonic_increasing}')

