import psutil
import logging


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
        print(message)

    def check_cpu_load(self):
        cpu_load = psutil.cpu_percent(interval=1)
        self.log(f'Current CPU Load is {cpu_load}%')
        return cpu_load

    def check_ram_load(self):
        ram_load = psutil.virtual_memory().percent
        self.log(f'Current RAM Load is {ram_load}%')
        return ram_load

    def monitor_system(self):
        cpu_load = self.check_cpu_load()
        ram_load = self.check_ram_load()
        self.log(f'Current CPU Load is {cpu_load}%')
        self.log(f'Current RAM Load is {ram_load}%')


if __name__ == '__main__':
    monitor = SystemMonitor()
    monitor.monitor_system()
