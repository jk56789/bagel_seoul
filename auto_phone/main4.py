from ppadb.client import Client

# ADB 클라이언트 초기화
client = Client(host='192.168.212.34', port=5555)
print("ADB 클라이언트 초기화 완료")

# 연결된 기기 목록 가져오기
devices = client.devices()
print("기기 목록 가져오기 완료")

# 이후의 코드 계속...
