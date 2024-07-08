from ppadb.client import Client
import time
import cv2


# ADB 서버와 연결
client = Client(host='127.0.0.1', port=5037)

# 연결된 디바이스 확인
devices = client.devices()
if len(devices) == 0:
    print('연결된 디바이스가 없습니다.')
    quit()

device = devices[1]  # 첫 번째 디바이스 사용

# 현재 시간을 기준으로 파일명 생성
timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
screenshot_filename = f'screenshot_{timestamp}.png'

# 스크린샷을 찍고 파일로 저장
result = device.screencap()
with open(screenshot_filename, 'wb') as f:
    f.write(result)

print(f'스크린샷이 {screenshot_filename}에 저장되었습니다.')

