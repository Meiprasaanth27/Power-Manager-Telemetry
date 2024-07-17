import psutil
import time
from pypapi import events, papi_high as high

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent + net_io.bytes_recv

def get_power_usage():
    high.start_counters([events.PAPI_TOT_INS, events.PAPI_TOT_CYC])
    x = [i ** 2 for i in range(1000)]
    counters = high.stop_counters()
    return counters

def collect_telemetry(duration=60, interval=1):
    telemetry_data = []
    start_time = time.time()
    while time.time() - start_time < duration:
        data_point = {
            'time': time.time(),
            'cpu_usage': get_cpu_usage(),
            'memory_usage': get_memory_usage(),
            'network_usage': get_network_usage(),
            'power_usage': get_power_usage()
        }
        telemetry_data.append(data_point)
        time.sleep(interval)
    return telemetry_data
