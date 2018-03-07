"""
importing socket module to use
networking features
"""
import socket
"""
setting timeout so that if the timeout exceeded
connection will be closed and an exception will
raised
"""
socket.setdefaulttimeout(5)
"""
using socket
"""
s=socket.socket()
"""
connecting to local computer to ftp service
on port 21
"""
s.connect(('127.0.0.1',21))
# s.connect(('p30download.com',21))

"""
getting the answere returned by ftp server
"""
ans = s.recv(1024)
"""
closing the socket
"""
s.close()
print(ans)