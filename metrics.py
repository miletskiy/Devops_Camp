#!/usr/bin/env python
# metrics.py

import psutil
import argparse

parser = argparse.ArgumentParser(description = 'Metrics collection script')
msg = 'Please use `cpu` for CPU metrics or `mem` for memory metrics'
parser.add_argument('type', type=str,
    help=f'Type of metric. {msg}')
args = parser.parse_args()


if args.type == 'cpu':

    cpu_result = psutil.cpu_times_percent()

    print(f'system.cpu.idle {cpu_result.idle}')
    print(f'system.cpu.user {cpu_result.user}')
    print(f'system.cpu.guest {cpu_result.guest}')
    print(f'system.cpu.iowait {cpu_result.iowait}')
    print(f'system.cpu.stolen {cpu_result.steal}')
    print(f'system.cpu.system {cpu_result.system}')

elif args.type == 'mem':
    mem_result = psutil.virtual_memory()
    swap_result = psutil.swap_memory()

    print(f'virtual total {mem_result.total}')
    print(f'virtual used {mem_result.used}')
    print(f'virtual free {mem_result.free}')
    print(f'virtual shared {mem_result.shared}')
    print(f'swap total {swap_result.total}')
    print(f'swap used {swap_result.used}')
    print(f'swap free {swap_result.free}')

else:
    print(msg)
