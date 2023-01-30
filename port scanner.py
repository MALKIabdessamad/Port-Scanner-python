import socket

def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

port = XPORT

ranges = [
    ('192.168.1', 256),
    ('10.0.0', 256),
    ('172.16', 16),
    ('172.31', 16),
]

with open("open_ports.txt", "w") as f:
    for prefix, size in ranges:
        for i in range(1, size+1):
            ip = f"{prefix}.{i}"
            if check_port(ip, port):
                f.write(f"{ip}:{port}\n")
                print(f"The port {port} is open on IP {ip}")
            else:
                print(f"The port {port} is closed on IP {ip}")
