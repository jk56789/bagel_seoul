from ppadb.client import Client
import time
import cv2
import numpy as np

# ADB 서버와 연결
client = Client(host='127.0.0.1', port=5037)

# 연결된 디바이스 확인
devices = client.devices()
if len(devices) == 0:
    print('연결된 디바이스가 없습니다.')
    quit()

# 디바이스를 두 그룹으로 나누기

#devices_CAMERA = [devices[9]] if len(devices) > 1 else []
devices_CAMERA = devices[6:13]




# 화면 켜기 함수
def wake_up():
    device.shell('input keyevent KEYCODE_POWER')
    time.sleep(0.5) 

# 홈화면으로 가기 함수
def press_home(device):
    
    device.shell('input keyevent KEYCODE_HOME')

# 특정 좌표 클릭 함수
def click_coordinates(device, x, y):
    device.shell(f'input tap {x} {y}')
    
# 화면 캡쳐 함수
def take_screenshot(device, filename):
    result = device.screencap()
    with open(filename, 'wb') as f:
        f.write(result)
        
        

#############################################################################
# 1.홈화면 가기
for device in devices_CAMERA:
    # 화면이 꺼져있는지 확인하고 켜기
    press_home(device) # 홈화면으로 이동하는 시간을 기다립니다. 필요에 따라 조정하세요.
    
# 1.|||
click_x = 241
click_y = 2328
for device in devices_CAMERA:
    click_coordinates(device, click_x, click_y)
    #time.sleep(1) 

click_x = 531
click_y = 1886
for device in devices_CAMERA:
    click_coordinates(device, click_x, click_y)
    print(f'1.모든 디바이스에 대해 모든 창 닫기')
    #time.sleep(0.5)
    
click_x = 916
click_y = 261
for device in devices_CAMERA:
    click_coordinates(device, click_x, click_y)
    print(f'2. 카메라 켜기')
    #time.sleep(0.5)

click_x = 747
click_y = 1801
for device in devices_CAMERA:
    click_coordinates(device, click_x, click_y)
    print(f'3. 비디오 변경')
    #time.sleep(0.5)