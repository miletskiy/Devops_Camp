
import psutil

print(psutil.cpu_times())


cpu_result = psutil.cpu_times_percent()

print(f'system.cpu.idle {cpu_result.idle}')
print(f'system.cpu.user {cpu_result.user}')
print(f'system.cpu.guest ')   # TODO
print(f'system.cpu.iowait ')  # TODO
print(f'system.cpu.stolen ')  # TODO
print(f'system.cpu.system {cpu_result.system}')
