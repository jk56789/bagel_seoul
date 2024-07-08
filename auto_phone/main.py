from ppadb.client import Client

client = Client(host = '127.0.0.1', port = 5037)


find_devices = client.devices()

if len(find_devices) == 0:
    print('NO DEVICES')
    quit()

device = find_devices[0]
print(device)
print(f'찾은 디바이스: {device}')