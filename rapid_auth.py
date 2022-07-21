import hwid
import crypting
import config
import requests

_hwid = hwid.get_hwid()

def login_user(username, password):
    url = 'http://localhost/testing/decrypt.php'
    post_data = {'encryptedtext': 'AwHKiHBpAtxeUr6s9WxMsVgd1DEjA/1FfJmwG0m9nTWfHVm9bNSTV54DXseb1M+R8SM2/SgrkwP4PPdZzND3YaJxKTG4/aZ7bm/kZHSkLZACeQ==',
    'password': 'this-is-my-password'}

    x = requests.post(url, data = post_data)

    print(x.text)
