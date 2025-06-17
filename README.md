# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTION

*NAME*: SIDDHESH DILIP REWALE

*INTERN ID*: CT04DG367

*DOMAIN*: Cyber Security & Ethical Hacking

*DURATION*: 4 weeks

*MENTOR*:  Neela Santhosh

🔐 Project: Penetration Testing Toolkit Using Python
📝 Description
The Penetration Testing Toolkit is a modular Python-based security suite designed to automate key stages of ethical hacking and vulnerability assessment. Developed within a Kali Linux environment, this tool focuses on three core functionalities: Port Scanning, Web Application Vulnerability Detection, and SSH Brute Force Attacks. It is intended to assist cybersecurity learners and professionals in conducting lightweight, transparent, and effective security tests on networks and web applications.

The toolkit was built to reflect real-world offensive security workflows, drawing inspiration from common tasks performed during the reconnaissance and exploitation phases of penetration testing. Instead of relying on complex tools that often act as black boxes, this project emphasizes hands-on scripting, offering insight into how low-level network and application vulnerabilities are discovered and exploited.

🛠️ Tools and Technologies Used
The toolkit is written in Python 3, leveraging its simplicity and vast ecosystem of security-related libraries. The socket module powers the custom Port Scanner, enabling TCP connection tests across common ports. The requests library and BeautifulSoup (bs4) are used in the Web Vulnerability Scanner, allowing for HTTP interactions and HTML parsing to detect and test form-based inputs. For SSH brute forcing, Paramiko is used to script automated login attempts with a supplied wordlist.

To improve performance, especially during port scanning, the toolkit uses ThreadPoolExecutor for concurrent execution. The entire toolset is designed to run efficiently in Kali Linux, a popular distribution for offensive security tasks. Development and version control were managed through Git and GitHub, ensuring the project is collaborative and easily extensible.

⚙️ How It Works
The toolkit accepts command-line arguments to specify which module to run. Each module is built to function independently while sharing a common interface.

Port Scanner: Connects to a specified IP and checks for open TCP ports in the range 1-1024. Multi-threading ensures fast and efficient scans.

Web Vulnerability Scanner: Takes a target URL, parses HTML for forms, and injects known SQL Injection (e.g., ' OR '1'='1) and XSS (e.g., <script>alert(1)</script>) payloads into input fields. It then examines the server’s response for signs of vulnerability.

SSH Brute Forcer: Attempts to guess the SSH password for a given host and username using a user-supplied wordlist. Successful attempts are reported, simulating unauthorized access testing.

Each module outputs meaningful results to help identify potential security issues. The design is intentionally simple and readable, making it ideal for learning and extending.

✅ Outcome
This project demonstrates the power of Python in building real-world security tools. It allowed for deeper understanding of how attacks such as port probing, injection, and brute force are carried out. The modularity of the code makes it easy to add new features like directory traversal, CSRF, or command injection in the future.

Overall, the toolkit serves as both a learning resource and a practical utility for early-stage penetration testing. It proves that with basic Python scripting, one can build tools that are both educational and functional in the field of cybersecurity.

![Image](https://github.com/user-attachments/assets/9506bffd-2c72-4632-ab96-0d563ea665b6)
