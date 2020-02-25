# metrics.py

import psutil


cpu_result = psutil.cpu_times_percent()

print(f'system.cpu.idle {cpu_result.idle}')
print(f'system.cpu.user {cpu_result.user}')
print(f'system.cpu.guest ')   # TODO
print(f'system.cpu.iowait ')  # TODO
print(f'system.cpu.stolen ')  # TODO
print(f'system.cpu.system {cpu_result.system}')


mem_result = psutil.virtual_memory()

print(f'virtual total {mem_result.total}')
print(f'virtual used {mem_result.used}')
print(f'virtual free {mem_result.free}')
print(f'virtual shared ') # TODO

swap_result = psutil.swap_memory()

print(f'swap total {swap_result.total}')
print(f'swap used {swap_result.used}')
print(f'swap free {swap_result.free}')
