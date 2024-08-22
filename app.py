import psutil
import logging
import time


def check_cpu_load():
    cpu_load = psutil.cpu_percent(interval=1, percpu=True)
    return cpu_load


class SystemMonitor:
    def __init__(self, log_file='/var/log/system_monitor.log'):
        self.log_file = log_file

        # Configure logging
        logging.basicConfig(
            filename=self.log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        )

    def log(self, message):
        logging.debug(message)
        # print(message)    # UNCOMMENT THIS LINE TO VIEW LOG MESSAGES IN THE CLI

    def check_ram_load(self):
        ram_load = psutil.virtual_memory().percent
        return ram_load

    def monitor_system(self):
        cpu_load = check_cpu_load()
        ram_load = self.check_ram_load()
        self.log(f'CPU {cpu_load}%    |    RAM {ram_load}%')


if __name__ == '__main__':
    monitor = SystemMonitor()
    while True:
        monitor.monitor_system()
        time.sleep(10)
