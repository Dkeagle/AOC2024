import functools
import time
import psutil

def resource_usage_monitor(func):
    """
    Decorator to monitor execution time and resource usage of a function

    Parameters:
    @func => function to monitor
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
       
        initial_memory = process.memory_info().rss
        initial_vms = process.memory_info().vms
        initial_cpu_times = process.cpu_times()
       
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
       
        final_memory = process.memory_info().rss
        final_vms = process.memory_info().vms
        final_cpu_times = process.cpu_times()
       
        box_width = 64

        print("\n" + "*" * (box_width + 4))
        print(f"* {f'Execution time: {end_time - start_time:.4f} seconds':<{box_width}} *")
        print(f"* {f'Memory usage: {(final_memory - initial_memory) / (1024 ** 2):.4f} MB':<{box_width}} *")
        print(f"* {f'Virtual memory usage: {(final_vms - initial_vms) / (1024 ** 2):.4f} MB':<{box_width}} *")
        print(f"* {f'CPU Time (User/System): {final_cpu_times.user - initial_cpu_times.user:.2f}s/{final_cpu_times.system - initial_cpu_times.system:.2f}s':<{box_width}} *")
        print("*" * (box_width + 4) + "\n")
       
        return result
   
    return wrapper