# main.py
import argparse
from modules import port_scanner, web_scanner, brute_forcer

def main():
    parser = argparse.ArgumentParser(description="Modular Pentest Tool")
    parser.add_argument('--module', required=True, choices=['port', 'web', 'brute'], help='Module to run')
    parser.add_argument('--target', required=True, help='Target IP or Host')
    parser.add_argument('--port', type=int, help='Port number for brute-forcing (SSH)')
    parser.add_argument('--username', help='Username for SSH brute-forcing')
    parser.add_argument('--wordlist', help='Wordlist file path for SSH brute-forcing')

    args = parser.parse_args()

    if args.module == 'port':
        port_scanner.scan(args.target)
    elif args.module == 'web':
        web_scanner.scan(args.target)
    elif args.module == 'brute':
        if args.port and args.username and args.wordlist:
            brute_forcer.ssh_brute(args.target, args.port, args.username, args.wordlist)
        else:
            print("[-] For brute module, --port, --username, and --wordlist are required.")
    else:
        print("[-] Invalid module specified.")

if __name__ == '__main__':
    main()

