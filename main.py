import sys
import threading

import requests

URL = 'http://211.170.25.198:10004'

class Worker(threading.Thread):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def run(self):
    print("sub thread start ", threading.currentThread().getName())
    payload = f'<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\r\n<m2m:cin xmlns:m2m=\"http://www.onem2m.org/xml/protocols\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\r\n    <ri>2</ri>\r\n    <con>{threading.currentThread().getName()}</con>\r\n</m2m:cin>'
    headers = {
      'Content-Type': 'application/xml'
    }
    response = requests.request("POST", URL, headers=headers, data=payload)
    print(response.text)
    print("sub thread end ", threading.currentThread().getName())


print("main thread start")
for j in range(10):
  for i in range(1000):
    name = "thread {}".format(i)
    t = Worker(name)                # sub thread 생성
    t.start()                       # sub thread의 run 메서드를 호출

print("main thread end")
