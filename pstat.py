import argparse
from time import sleep, time
from helper import *


def parse_args():
    parser = argparse.ArgumentParser(prog='pstat', description='Provides process stats at regular interval')
    parser.add_argument('-n', '--name', type=str, help='name of the process', required=True)
    parser.add_argument('-d', '--duration', type=int, help='total monitoring duration in seconds', required=True)
    parser.add_argument('-i', '--interval', type=int, help='sampling interval in seconds (default: 5s)', default=5)
    return parser.parse_args()


def pstat():
    args = parse_args()
    pids = get_associated_pids(args.name)
    create_files(args.name, pids)
    start_time = time()
    while (time() - start_time) < args.duration:
        for pid in pids:
            fname = f'{args.name}_{pid}.csv'
            metrics = get_metrics(pid)
            process_metrics(f'{args.name} [pid: {pid}]', metrics, fname)
        sleep(args.interval)


if __name__ == '__main__':
    pstat()
