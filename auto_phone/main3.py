from ppadb.client import Client

# ADB 클라이언트 초기화
client = Client(host='192.168.212.34', port=5555)

# 연결된 기기 목록 가져오기
devices = client.devices()
print("프로그램이 시작되었습니다.")
if len(devices) == 0:
    print("No devices connected")
else:
    for device in devices:
        print(f"Connected device: {device.serial}")

        # 예시: 기기에서 화면 캡처 및 다운로드
        device.screencap('/sdcard/screenshot.png')
        device.pull('/sdcard/screenshot.png', 'C:/Users/user/Desktop/screenshot.png')

