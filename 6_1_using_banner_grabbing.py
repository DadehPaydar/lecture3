import socket
socket.setdefaulttimeout(5)
s=socket.socket()
s.connect(("127.0.0.1",21))
ans=s.recv(1024)
ans=str(ans)
if "FreeFloat Ftp Server (Version 1.00)" in ans:
    print("[+] FreeFloat server is vulnerable ")
elif "3Com 3CDaemon FTP Server Version 2.0" in ans:
    print("[+] 3CDaemon server is vulnerable ")
elif "Ability Server 2.34" in ans:
    print("[+] Ability server is vulnerable ")
elif "Sami FTP Server 2.0.2" in ans:
    print("[+] Sami server is vulnerable ")
else:
    print("[-] FTP server is not vulnerable")