import socket



def openserver(ip  ,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip , port))
    s.listen(1)
    conn, addr = s.accept()
    return conn, addr


def trapping(conn, addr):
    print("[+] 트랩 걸림!!!, ", addr)
    while True:
        output = conn.recv(65535).decode()
        print(output)
        ta = input("EXIT? : ")
        if(ta == "exit"):
            conn.send(b'exit')
            conn.close()
        







if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 4444
    conn, addr = openserver(ip , port)
    trapping(conn, addr)