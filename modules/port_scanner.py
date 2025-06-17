# modules/port_scanner.py
import socket
from concurrent.futures import ThreadPoolExecutor

def scan(target):
    print(f"[+] Scanning {target} for open ports...")

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
        except:
            pass

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, port)
