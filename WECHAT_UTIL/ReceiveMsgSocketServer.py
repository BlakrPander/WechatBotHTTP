#coding=gbk
import socketserver
import json
from WECHAT_UTIL.MessageProcess import messageProcess as msgProcess

class ReceiveMsgSocketServer(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        conn = self.request
        while True:
            try:
                ptr_data = b""
                while True:
                    data = conn.recv(1024)
                    ptr_data += data
                    if len(data) == 0 or data[-1] == 0xA:
                        break
                msg = json.loads(ptr_data.decode('utf-8'))
                ReceiveMsgSocketServer.msg_callback(msg)
            except OSError:
                break
            except json.JSONDecodeError:
                pass
            conn.sendall("200 OK".encode())
        conn.close()

    @staticmethod
    def msg_callback(msg):
        msgProcess(msg)
        # TODO: 在这里写额外的消息处理逻辑


if __name__ == "__main__":
    ReceiveMsgSocketServer.msg_callback({"123":"234"})
    print("OK")