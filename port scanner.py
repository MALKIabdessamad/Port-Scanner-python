import socket
import threading

def check_port(ip, port, results):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        s.close()
        results.append((ip, port, True))
    except:
        results.append((ip, port, False))

port = input("Enter the port number to check: ")

ip_range = input("Enter the IP address range to check (e.g. 192.168.1, 256): ")
prefix, size = ip_range.split(',')
size = int(size)

output_file = f"open_ports_{prefix}_{size}.txt"

threads = []
results = []

for i in range(1, size+1):
    ip = f"{prefix}.{i}"
    t = threading.Thread(target=check_port, args=(ip, int(port), results))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

with open(output_file, "w") as f:
    for ip, port, is_open in results:
        if is_open:
            f.write(f"{ip}:{port}\n")
            print(f"The port {port} is open on IP {ip}")
        else:
            print(f"The port {port} is closed on IP {ip}")
