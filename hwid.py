import cpuinfo
import os
import GPUtil
import winreg
from tabulate import tabulate

def read_reg(k):
    try:
        key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\")
        value = winreg.QueryValueEx(key,k)
        if key:
            winreg.CloseKey(key)
        return value[0]
    except Exception as e:
        print(e)
    return None


def get_hwid():
    windows_username = os.getlogin()
    gpu_name = ""
    gpu_memory = ""
    drive_count = 0
    cpu_name = cpuinfo.get_cpu_info()['brand_raw']
    cpu_cores = cpuinfo.get_cpu_info()['count']
    os_caption = read_reg('ProductName')
    os_serial_number = read_reg('ProductId')



    drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]

    for drive in drives:
        drive_count = drive_count + 1


    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        gpu_name = gpu.name
        gpu_memory = f"{gpu.memoryTotal}MB"

    hwid_array = {"windows_username": windows_username, "gpu_name": gpu_name, "gpu_memory": gpu_memory, "drive_count": drive_count, "cpu_name": cpu_name, "cpu_cores": cpu_cores, "os_caption": os_caption, "os_serial_number": os_serial_number}
    return hwid_array
