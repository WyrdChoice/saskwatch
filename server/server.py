import asyncio
import json
from threading import Thread
import threading
from BLE import uart_terminal
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write(b"Hello, World!")

        if self.path == "/":
            self.path = "/index.html"

        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(latestData), "utf-8"))
            return

        if self.path == "/end":
            httpd.server_close()

        if not self.path.startswith("/static/"):
            self.path = "/static" + self.path

        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(file_to_open, "utf-8"))
        except:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 - Not Found")


latestData = [{"balloon module loading": True}, {"ground module loading": True}]
connected = False


def full_msg(msg):
    global latestData
    try:
        msgData = json.loads(msg)
        latestData[msgData["moduleID"] - 1] = msgData
        print("latestData", msgData)
    except:
        print(f"ERROR: {msg}")


def setConnected(isConnected):
    global connected
    # print("connected", connected)
    connected = isConnected

    # def connect():
    #     if connected:
    #         return
    #     print("Interval reached and not connected. Attempting connection")


thread1 = threading.Thread(
    target=asyncio.run,
    args=(
        uart_terminal(full_msg, setConnected, "GroundModuleBLE"),
    ),  # NEED BOTH WEIRD COMMAS
)
thread2 = threading.Thread(
    target=asyncio.run,
    args=(
        uart_terminal(full_msg, setConnected, "BalloonModuleBLE"),
    ),  # NEED BOTH WEIRD COMMAS
)
try:
    thread1.start()
    thread2.start()
except asyncio.CancelledError as e:
    print(e)


# from threading import Timer


# def interval_connect():
#     connect()
#     Timer(15.0, interval_connect).start()


# Timer(0.0, interval_connect).start()


httpd = HTTPServer(("", 3000), SimpleHTTPRequestHandler)
try:
    print("Listening at http://localhost:3000/")
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
