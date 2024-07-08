from ppadb.client import Client
import time

def adb_connect():
    client = Client(host = '192.168.212.34', port = 44427)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('NO DEVICES')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')
    
    return device, client 

device, client = adb_connect()

device.shell('input keyevent 64')
time.sleep(1.0)

xyPosition = '423 136'
device.shell(f'input tap {xyPosition}')
time.sleep(1.0)

url = 'www.naver.com'
device.shell(f'input text {url}')
time.sleep(1.0)

device.shell('input keyevent 66')
time.sleep(1.0)


