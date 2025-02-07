import time
from obswebsocket import obsws, requests

host = 'localhost' #
port = 4444
password = 'your_password'

ws = obsws(host, port, password)
ws.connect()

stream_key = "1"

stream_settings = {
    'server': 'rtmp://a.rtmp.youtube.com/live2',
    'key': stream_key,
}

ws.call(requests.SetStreamSettings(
    stream_settings['server'],
    stream_settings['key'],
    use_auth=True
))

ws.call(requests.StartStreaming())

print("start")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    ws.call(requests.StopStreaming())
    print("Streaming stopped.")
    ws.disconnect()
