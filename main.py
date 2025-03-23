import ctypes
import threading
import socketserver
import psutil

from WECHAT_UTIL.util.tmpfunctions.fixVersion import fixVersion

from WECHAT_UTIL import WECHAT_HTTP_APIS
from WECHAT_UTIL import WECHAT_HTTP_API_PARAM_TEMPLATES
from WECHAT_UTIL import WECHAT_HTTP_API_OP
from WECHAT_UTIL import ReceiveMsgSocketServer

if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_ulonglong):
    driver = ctypes.cdll.LoadLibrary('./lib/wxDriver64.dll')
else:
    driver = ctypes.cdll.LoadLibrary('./lib/wxDriver.dll')

new_wechat = driver.new_wechat
new_wechat.argtypes = None
new_wechat.restype = ctypes.c_int

start_listen = driver.start_listen
start_listen.argtypes = [ctypes.c_int, ctypes.c_int]
start_listen.restype = ctypes.c_int

stop_listen = driver.stop_listen
stop_listen.argtypes = [ctypes.c_int]
stop_listen.restype = ctypes.c_int

APIS = WECHAT_HTTP_APIS()
get_http_template = WECHAT_HTTP_API_PARAM_TEMPLATES().get_http_template
post_wechat_http_api = WECHAT_HTTP_API_OP().post_wechat_http_api
get_wechat_hhtp_api = WECHAT_HTTP_API_OP().get_wechat_http_api


def get_wechat_pid_list() -> list:  # 从进程中寻找微信进程
    pid_list = []
    process_list = psutil.pids()
    for pid in process_list:
        try:
            if psutil.Process(pid).name() == 'WeChat.exe':
                pid_list.append(pid)
        except psutil.NoSuchProcess:
            pass
    return pid_list

    # wangziqiong="love"
    # love = "wzq"


def start_socket_server(port: int = 10808,
                        request_handler=ReceiveMsgSocketServer,
                        main_thread: bool = True) -> int or None:
    ip_port = ("127.0.0.1", port)
    try:
        print(1)
        s = socketserver.ThreadingTCPServer(ip_port, request_handler)
        if main_thread:
            s.serve_forever()
        else:
            socket_server = threading.Thread(target=s.serve_forever)
            socket_server.setDaemon(True)
            socket_server.start()
            return socket_server.ident
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    return None


if __name__ == '__main__':
    port = 8000
    pids = get_wechat_pid_list()
    print("Launching WeChat")
    if len(pids) == 0:
        pids.append(new_wechat())  # 当没有微信进程时 重新创建一个

    print("Fixing WeChat Version")
    fixVersion("3.9.10.19")

    start_listen(pids[0], port)  # 开启监听
    post_wechat_http_api(APIS.WECHAT_LOG_START_HOOK, port)
    print(post_wechat_http_api(APIS.WECHAT_GET_SELF_INFO, port))
    post_wechat_http_api(APIS.WECHAT_MSG_START_HOOK, port, {"port": 10808})
    start_socket_server()
    stop_listen(pids[0])
