# modules/web_scanner.py
import requests

def scan(target):
    print(f"[+] Scanning {target} for common web vulnerabilities...")
    payloads = ["' OR '1'='1", "<script>alert(1)</script>"]
    error_signatures = ["sql syntax", "mysql", "syntax error", "unexpected token", "unterminated string", "warning", "alert(1)"]

    for payload in payloads:
        try:
            response = requests.get(f"http://{target}/?q={payload}", timeout=5)
            content = response.text.lower()
            for error in error_signatures:
                if error in content:
                    print(f"[!] Potential vulnerability found with payload: {payload} (Detected: {error})")
                    break
        except requests.RequestException:
            print(f"[!] Failed to connect to {target}")
