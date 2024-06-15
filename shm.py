import psutil
import subprocess

# Define thresholds
CPU_THRESHOLD = 80  # percent
MEMORY_THRESHOLD = 80  # percent
DISK_THRESHOLD = 80  # percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"CPU usage is high: {cpu_usage}%")

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"Memory usage is high: {memory_usage}%")

def check_disk_usage():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            disk_usage = psutil.disk_usage(partition.mountpoint).percent
            if disk_usage > DISK_THRESHOLD:
                print(f"Disk usage on {partition.mountpoint} is high: {disk_usage}%")
        except PermissionError:
            # Skip partitions that are not accessible
            continue

def check_running_processes():
    running_processes = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    print("Running processes:\n", running_processes.stdout)

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
