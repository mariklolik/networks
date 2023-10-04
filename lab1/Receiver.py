import socket
import struct


class Receiver:
    def __init__(self, multicast_group, port):
        self.multicast_group = multicast_group
        self.port = port
        # AF_INET - IPv4 protocol, SOCK_DGRAM - datagram UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', self.port))
        # string address to binary address
        group = socket.inet_aton(self.multicast_group)
        # format to pack data to binary form 4 bytes string - 1st arg, L - long for socket.INADDR_ANY
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        # configure socket to listen multicast group
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def receive_messages(self):
        while True:
            data, address = self.sock.recvfrom(1024)
            print(f'Received: {data.decode()} from {address}')

    def close(self):
        self.sock.close()
