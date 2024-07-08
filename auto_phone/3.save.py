from ppadb.client import Client
import time
import cv2
import numpy as np
import os

# ADB 서버와 연결
client = Client(host='127.0.0.1', port=5037)

# 연결된 디바이스 확인
devices = client.devices()
if len(devices) == 0:
    print('연결된 디바이스가 없습니다.')
    quit()

# 디바이스를 두 그룹으로 나누기
'''devices_ML = [devices[0]] if len(devices) > 0 else []
devices_CAMERA = [devices[1]] if len(devices) > 1 else []'''
devices_CAMERA = devices[6:13]
devices_ML = devices[:6]

# 특정 좌표 클릭 함수
def click_coordinates(device, x, y):
    device.shell(f'input tap {x} {y}')
    
# 화면 캡쳐 함수
def take_screenshot(device, filename):
    result = device.screencap()
    with open(filename, 'wb') as f:
        f.write(result)
        


# 5. go pose detection   
click_x = 420
click_y = 2165
for device in devices_ML:
    click_coordinates(device, click_x, click_y)
    print(f'클릭 완료: x={click_x}, y={click_y}')
    #time.sleep(1) 

click_x = 538
click_y = 2023
for device in devices_CAMERA:
    click_coordinates(device, click_x, click_y)
    print(f'4. 녹화 시작')
    #time.sleep(1)

# 입력 대기 코드
input("저장중입니다... 종료하려면 아무 키나 입력하세요...")

click_x = 420
click_y = 2165
for device in devices_ML:
    click_coordinates(device, click_x, click_y)
    print(f'클릭 완료: x={click_x}, y={click_y}')


click_x = 623
click_y = 2039
for device in devices_CAMERA:
    click_coordinates(device, click_x, click_y)
    print(f'4. 녹화 종료')
    #time.sleep(1)

