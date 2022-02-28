import sipfullproxy
from sipfullproxy import *
import socket
import socketserver

hostname = socket.gethostname()
print("Launching SIP Proxy using " + hostname)
ipaddress = socket.gethostbyname(hostname)
print("IP Address: " + ipaddress)
sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
server = socketserver.UDPServer((HOST, PORT), UDPHandler)
print("SIP Proxy running...")
server.serve_forever()
