import hwid
import crypting
import config
import requests

_hwid = hwid.get_hwid()

def sign_in_user(username, password):
    url = 'http://localhost/rapid_auth_api/loader_users/sign_in.php'
    post_data = {'api_key': config.api_key,
    'username': crypting.encrypt_data(username),
    'password': crypting.encrypt_data(password),
    'windows_username': crypting.encrypt_data(_hwid["windows_username"]),
    'gpu_name': crypting.encrypt_data(_hwid["gpu_name"]),
    'gpu_ram': crypting.encrypt_data(_hwid["gpu_memory"]),
    'drive_count': crypting.encrypt_data(str(_hwid["drive_count"])),
    'cpu_name': crypting.encrypt_data(_hwid["cpu_name"]),
    'cpu_cores': crypting.encrypt_data(str(_hwid["cpu_cores"])),
    'os_caption': crypting.encrypt_data(_hwid["os_caption"]),
    'os_serial_number': crypting.encrypt_data(_hwid["os_serial_number"])
    }

    x = requests.post(url, data = post_data)

    return crypting.decrypt_data(x.text)



def sign_up_user(username, password):
    url = 'http://localhost/rapid_auth_api/loader_users/sign_up.php'
    post_data = {'api_key': config.api_key,
    'username': crypting.encrypt_data(username),
    'password': crypting.encrypt_data(password),
    'windows_username': crypting.encrypt_data(_hwid["windows_username"]),
    'gpu_name': crypting.encrypt_data(_hwid["gpu_name"]),
    'gpu_ram': crypting.encrypt_data(_hwid["gpu_memory"]),
    'drive_count': crypting.encrypt_data(str(_hwid["drive_count"])),
    'cpu_name': crypting.encrypt_data(_hwid["cpu_name"]),
    'cpu_cores': crypting.encrypt_data(str(_hwid["cpu_cores"])),
    'os_caption': crypting.encrypt_data(_hwid["os_caption"]),
    'os_serial_number': crypting.encrypt_data(_hwid["os_serial_number"])
    }

    x = requests.post(url, data = post_data)

    return  crypting.decrypt_data(x.text)



def get_active_keys(username, password):
    url = 'http://localhost/rapid_auth_api/loader_users/get_active_keys.php'
    post_data = {'api_key': config.api_key,
    'username': crypting.encrypt_data(username),
    'password': crypting.encrypt_data(password)
    }

    x = requests.post(url, data = post_data)

    return crypting.decrypt_data(x.text)



def redeem_license_key(username, password, license_key):
    url = 'http://localhost/rapid_auth_api/loader_users/redeem_key.php'
    post_data = {'api_key': config.api_key,
    'username': crypting.encrypt_data(username),
    'password': crypting.encrypt_data(password),
    'license_key': crypting.encrypt_data(license_key)
    }

    x = requests.post(url, data = post_data)

    return crypting.decrypt_data(x.text)

